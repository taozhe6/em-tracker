import os
from typing import Optional

import requests

# 颜色定义
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_RED = "\033[31m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE = "\033[34m"
C_CYAN = "\033[36m"


def perform_login(account: dict) -> Optional[requests.Session]:
    """执行登录操作，成功返回 session，失败返回 None。"""
    LOGIN_URL = "https://www.editorialmanager.com/j.asp?a=e"
    session = requests.Session()
    session.headers.update({
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    })
    payload = {
        "a": "l",
        "p": account['password'],
        "u": account['username'],
        "jr": account['journal_short_name']
    }
    try:
        response = session.post(LOGIN_URL, data=payload, timeout=15)
        response.raise_for_status()
        if "Invalid login" in response.text or "Login failed" in response.text:
            return None
        return session
    except requests.RequestException as error:
        print(C_RED + f"\n[网络错误] 登录请求失败: {error}")
        return None


def update_config_file(new_account: dict) -> bool:
    """安全地读取、更新并写回 config.py 文件，保持一致的键顺序。"""
    config_path = 'config.py'
    print(C_BLUE + f"\n[配置更新] 正在向 {config_path} 添加新账户...")
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        insertion_index = -1
        for i, line in reversed(list(enumerate(lines))):
            if line.strip() == ']':
                insertion_index = i
                break

        if insertion_index == -1:
            print(C_RED + f"[错误] 未能在 {config_path} 中找到 'ACCOUNTS = [...]' 的有效结构。")
            return False

        new_entry_str = (
            f"    {{\n"
            f"        'journal_short_name': '{new_account['journal_short_name']}',\n"
            f"        'journal_full_name': '{new_account['journal_full_name']}',\n"
            f"        'username': '{new_account['username']}',\n"
            f"        'password': '{new_account['password']}'\n"
            f"    }},\n"
        )

        lines.insert(insertion_index, new_entry_str)

        with open(config_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        print(C_GREEN + C_BOLD + "[成功] " + C_GREEN + "新账户配置已成功保存！")
        return True

    except FileNotFoundError:
        print(C_RED + f"[致命错误] {config_path} 文件未找到。")
        return False
    except Exception as error:
        print(C_RED + f"[致命错误] 更新配置文件时发生错误: {error}")
        return False


def run_config_adder():
    """引导用户添加新账户，保持与 config.py 一致的风格。"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + C_CYAN + "=" * 60)
    print(C_CYAN + C_BOLD + " EM/PM 账户配置增加器 (v2.2 - 格式统一版)")
    print(C_CYAN + "=" * 60)

    try:
        from config import ACCOUNTS
    except (ImportError, SyntaxError):
        print(C_YELLOW + "[提示] 未找到或无法解析 config.py，将假定无现有配置。")
        ACCOUNTS = []

    print(C_BLUE + "\n请输入新账户的四项信息:")
    new_account = {
        'journal_short_name': input(f"  - {C_CYAN}期刊简称 (例如 'GASTRO'): {C_RESET}").strip().upper(),
        'journal_full_name': input(f"  - {C_CYAN}期刊全名 (例如 'Gastroenterology'): {C_RESET}").strip(),
        'username': input(f"  - {C_CYAN}用户名: {C_RESET}").strip(),
        'password': input(f"  - {C_CYAN}密码 (输入时可见): {C_RESET}")
    }

    if not all(new_account.values()):
        print(C_RED + "\n[错误] 所有字段均为必填项，不能为空。操作已取消。")
        return

    for acc in ACCOUNTS:
        existing_user = acc.get('username', '').lower()
        new_user = new_account['username'].lower()
        existing_journal = acc.get('journal_short_name', '').lower()
        new_journal = new_account['journal_short_name'].lower()

        if existing_user == new_user and existing_journal == new_journal:
            print(C_RED + C_BOLD + "\n[错误] 配置已存在！" + C_RESET)
            print(f"{C_YELLOW}  -> 用户 '{new_account['username']}' 的期刊 "
                  f"'{new_account['journal_short_name']}' 已保存在 config.py 中。")
            print(C_RED + "操作已取消，未做任何修改。")
            return

    print(C_BLUE + "\n[验证] 正在使用您提供的信息尝试登录...")
    session = perform_login(new_account)

    if session:
        update_config_file(new_account)
    else:
        print(C_RED + "\n[操作取消] 由于登录验证失败，新账户未被添加到配置文件。")


if __name__ == "__main__":
    try:
        run_config_adder()
    except KeyboardInterrupt:
        print(C_YELLOW + "\n\n操作被用户中断。")
    except Exception as error:
        print(C_RED + C_BOLD + f"\n[未处理的致命错误] 发生了一个意外错误: {error}")
    finally:
        input("\n按 Enter 键退出...")
