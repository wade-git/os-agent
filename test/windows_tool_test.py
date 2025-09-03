import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from windows.agent.tools.service import launch_tool
from windows.desktop.service import Desktop

def main():
    # 创建 Desktop 实例
    desktop = Desktop()

    # TEST for launch_tool
    result = launch_tool.invoke({"name": "记事本", "desktop": desktop})
    print(f"Launch result: {result}")

if __name__ == "__main__":
    main()
