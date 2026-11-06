import os
import sys
import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest

ROOT_DIR = Path(__file__).parent.parent.parent
WEBUI_MAIN = ROOT_DIR / "webui" / "Main.py"
STYLES_CSS = ROOT_DIR / "webui" / "styles.css"


class TestWorkspaceSidebar(unittest.TestCase):
    def test_sidebar_styles_css_rules(self):
        """验证 styles.css 包含完整的专业工作台侧边栏规则。"""
        self.assertTrue(STYLES_CSS.exists(), f"styles.css not found at {STYLES_CSS}")
        content = STYLES_CSS.read_text(encoding="utf-8")

        # 1. 验证原生单选圆圈隐藏规则
        self.assertIn('div[data-testid="stRadio"] input[type="radio"]', content)
        self.assertIn('div[data-testid="stRadio"] label > span:first-child', content)
        self.assertIn('div[data-testid="stRadio"] label > div > div > div:first-child:not([data-testid="stMarkdownContainer"])', content)
        self.assertIn('display: none !important', content)

        # 2. 验证左侧激活指示条 (Active Indicator Strip)
        self.assertIn('label[data-selected="true"] > div::before', content)
        self.assertIn('label:has(input:checked) > div::before', content)
        self.assertIn('width: 3.5px !important', content)

        # 3. 验证悬浮动效 (Hover)
        self.assertIn('label:hover > div', content)
        self.assertIn('transform: translateX(2px) !important', content)

        # 4. 验证导航分组副标题 (Section Headers)
        self.assertIn('概览总控 · OVERVIEW', content)
        self.assertIn('核心工坊 · WORKFLOW', content)
        self.assertIn('系统与偏好 · SYSTEM', content)

        # 5. 验证科技感动态呼吸状态指示灯动画
        self.assertIn('@keyframes wsPulseIdle', content)
        self.assertIn('@keyframes wsPulseActive', content)

        # 6. 验证全宽布局与角标文字防重叠安全间距
        self.assertIn('align-items: stretch !important', content)
        self.assertIn('padding-right: 3.8rem !important', content)

        # 7. 验证暗黑模式适配（媒体查询与主题属性）
        self.assertIn('@media (prefers-color-scheme: dark)', content)
        self.assertIn('[data-theme="dark"]', content)

        # 8. 验证侧边栏折叠唤出控件（防止折叠后无法重新展开）
        self.assertIn('div[data-testid="stSidebarCollapsedControl"]', content)
        self.assertIn('pointer-events: auto !important', content)
        self.assertIn('展开工作台导航', content)
        self.assertNotIn('header[data-testid="stHeader"] {\n    display: none !important', content)

    def test_sidebar_app_integration(self):
        """验证侧边栏在 Streamlit AppTest 环境下的集成与状态联动。"""
        app = AppTest.from_file(str(WEBUI_MAIN), default_timeout=30)
        app.run()
        self.assertFalse(app.exception, f"App execution failed with: {app.exception}")

        # 验证侧边栏单选导航存在且选项数量为 6
        radio = app.sidebar.radio("workspace_active_view_radio")
        self.assertIsNotNone(radio, "workspace_active_view_radio not found in sidebar")
        self.assertEqual(len(radio.options), 6)
        self.assertEqual(radio.value, "dashboard")

        # 验证布局模式选择器存在
        mode_select = app.sidebar.selectbox("workspace_layout_mode_selector")
        self.assertIsNotNone(mode_select, "workspace_layout_mode_selector not found in sidebar")
        self.assertEqual(len(mode_select.options), 2)

        # 验证切换视图时状态同步
        radio.set_value("script").run()
        self.assertEqual(app.session_state["workspace_active_view"], "script")
        self.assertEqual(radio.value, "script")

        radio.set_value("settings").run()
        self.assertEqual(app.session_state["workspace_active_view"], "settings")
        self.assertEqual(radio.value, "settings")

    def test_dashboard_with_tasks_no_duplicate_element_key(self):
        """验证存在历史任务时，仪表盘与顶部任务管理 popover 同时渲染不会触发 DuplicateElementKey。"""
        fake_task = {
            "task_id": "mock_task_001",
            "task_path": str(ROOT_DIR),
            "state": 2,
            "progress": 100,
            "subject": "测试视频任务",
            "mtime": 1700000000,
            "video_file": "",
        }
        from app.services import state as sm
        with unittest.mock.patch.object(sm.state, "get_all_tasks", return_value=([fake_task], 1)):
            app = AppTest.from_file(str(WEBUI_MAIN), default_timeout=30)
            app.run()
            self.assertFalse(app.exception, f"App execution with tasks failed with: {app.exception}")


if __name__ == "__main__":
    unittest.main()
