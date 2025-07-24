<div align="center">

# 📄 Editorial Manager Tracker

**🔬 专业的学术期刊稿件状态自动追踪工具**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Made for Researchers](https://img.shields.io/badge/Made%20for-Researchers-orange.svg)](https://github.com/taozhe6/em-tracker)

[快速开始](#-快速开始) •
[功能演示](#-功能演示) •
[安装指南](#-安装指南) •
[使用文档](#-使用文档) •
[常见问题](#-常见问题)

---

**📊 专为使用 Editorial Manager 系统的学术期刊设计，让稿件追踪变得简单高效**

*支持 Gastroenterology、The Lancet 系列、American Journal of Gastroenterology 等数百种期刊*

</div>

## 🚀 快速开始

### ⚡ 三步启动

```bash
# 1. 克隆项目
git clone https://github.com/taozhe6/em-tracker.git
cd em-tracker

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置并运行
python add_config.py  # 添加期刊账户
python main.py        # 开始追踪
```

### 🎯 首次使用

```bash
# 创建虚拟环境（推荐）
python -m venv em-tracker-env
source em-tracker-env/bin/activate  # Linux/macOS
# em-tracker-env\Scripts\activate   # Windows

# 一键安装
pip install -r requirements.txt && python add_config.py
```

## 📺 功能演示

<div align="center">

### 🖥️ 命令行界面
*清晰的彩色输出，实时显示追踪进度*

### 📊 Excel报告示例
*自动生成的专业追踪报告*

| 时间戳 | 投稿日期 | 状态日期 | 当前状态 | 稿件编号 |
|--------|----------|----------|----------|----------|
| 2024-01-15 10:30 | 2024-01-10 | 2024-01-15 | Under Review | MS2024-001 |
| 2024-01-20 09:15 | 2024-01-10 | 2024-01-19 | Decision Made | MS2024-001 |

### 📁 智能文件组织
```
data/
├── researcher1@university.edu/
│   ├── MS2024-001_Innovative-Treatment-Approach/
│   │   └── Innovative-Treatment-Approach_投稿追踪.xlsx
│   └── MS2024-002_Clinical-Trial-Results/
│       └── Clinical-Trial-Results_投稿追踪.xlsx
└── researcher2@hospital.org/
    └── ...
```

</div>

## ✨ 核心功能

<table>
<tr>
<td width="50%">

### 🎯 智能追踪
- ✅ **自动状态检测** - 智能识别稿件状态变化
- ✅ **历史记录管理** - 完整的时间线追踪
- ✅ **多期刊支持** - 支持所有EM系统期刊
- ✅ **批量处理** - 一次查询所有稿件

</td>
<td width="50%">

### 📊 专业报告
- ✅ **Excel格式输出** - 专业格式化表格
- ✅ **自动文件管理** - 智能文件夹组织
- ✅ **状态变更提醒** - 高亮显示重要变化
- ✅ **数据持久化** - 安全的本地存储

</td>
</tr>
<tr>
<td width="50%">

### 🔒 隐私安全
- ✅ **本地数据存储** - 所有数据保存在本地
- ✅ **临时账户模式** - 无需保存敏感信息
- ✅ **配置文件保护** - 自动忽略敏感配置
- ✅ **网络安全** - 模拟真实浏览器请求

</td>
<td width="50%">

### 🛠️ 用户体验
- ✅ **彩色命令行** - 友好的视觉反馈
- ✅ **智能重试** - 网络异常自动恢复
- ✅ **交互式配置** - 向导式设置流程
- ✅ **错误处理** - 详细的错误信息和解决建议

</td>
</tr>
</table>

## 🌍 支持的期刊

### 🏥 医学期刊（已测试）

<div align="center">

| 期刊类别 | 期刊名称 | 简称 | 状态 |
|----------|----------|------|------|
| **消化内科** | Gastroenterology | `GASTRO` | ✅ 完全支持 |
| **消化内科** | Gut | `GUT` | ✅ 完全支持 |
| **消化内科** | American Journal of Gastroenterology | `AJG` | ✅ 完全支持 |
| **消化内科** | Inflammatory Bowel Diseases | `IBD` | ✅ 完全支持 |
| **综合医学** | The Lancet | `LANCET` | ✅ 完全支持 |
| **综合医学** | The Lancet Gastroenterology & Hepatology | `LANGAS` | ✅ 完全支持 |

</div>

> 💡 **支持所有使用 Editorial Manager 系统的期刊** - 只需要找到期刊的EM简称即可

### 🔍 如何找到期刊简称？

查看期刊的EM登录页面URL：
- `https://www.editorialmanager.com/gastro/` → 简称: `GASTRO`
- `https://www.editorialmanager.com/ibd/` → 简称: `IBD`

## 📦 安装指南

### 系统要求

- **Python**: 3.7+ 
- **操作系统**: Windows / macOS / Linux
- **网络**: 稳定的互联网连接

### 方式一：标准安装（推荐）

```bash
# 克隆项目
git clone https://github.com/taozhe6/em-tracker.git
cd em-tracker

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

### 方式二：直接下载

1. 点击 [Download ZIP](https://github.com/taozhe6/em-tracker/archive/main.zip)
2. 解压到本地文件夹
3. 进入文件夹运行：`pip install -r requirements.txt`

### 方式三：开发者安装

```bash
# Fork 项目后克隆
git clone https://github.com/YOUR_USERNAME/em-tracker.git
cd em-tracker

# 安装开发依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 如果有的话
```

## 📖 使用文档

### 🎯 基本工作流程

```mermaid
graph TD
    A[启动程序] --> B[选择用户]
    B --> C[选择期刊]
    C --> D[自动登录]
    D --> E[获取稿件状态]
    E --> F[对比历史记录]
    F --> G{状态是否变化?}
    G -->|是| H[更新Excel文件]
    G -->|否| I[显示无变化]
    H --> J[完成]
    I --> J
```

### 🔧 配置账户

#### 使用配置助手（推荐）

```bash
python add_config.py
```

按提示输入：
- **期刊全名**: `Gastroenterology`
- **期刊简称**: `GASTRO` 
- **用户名**: 您的EM账户用户名
- **密码**: 您的EM账户密码

#### 手动配置

创建 `config.py` 文件：

```python
ACCOUNTS = [
    {
        'journal_short_name': 'GASTRO',
        'journal_full_name': 'Gastroenterology',
        'username': 'your_username',
        'password': 'your_password'
    },
    # 可以添加多个期刊账户
]
```

### 🚀 运行程序

```bash
python main.py
```

程序将显示交互式菜单：

```
============================================================
 Journal Manuscript Tracker (v31.1)
============================================================

请选择要查询的用户:
  [1] researcher@university.edu (3本期刊)
  [2] doctor@hospital.org (1本期刊)
  [3] 手动输入临时账户进行查询
  [Q] 退出程序

请输入您的选择:
```

### 📊 理解输出结果

#### 🟢 成功案例
```
[步骤 1] 正在初始化登录流程...
正在尝试登录 'Gastroenterology'...
  - 第 1 次尝试...

[成功] 登录成功！

[步骤 2] 正在获取主菜单页面...
  - 成功！已获取主菜单HTML。

--- 正在处理: Innovative Treatment Approach for IBD... (MS#: MS2024-001) ---
  - [状态更新!] 发现新状态或状态日期变更。
    - 旧状态: Under Review (2024-01-15)
    - 新状态: Decision Made (2024-01-20)
    - 历史记录已更新并重新格式化: Innovative-Treatment-Approach_投稿追踪.xlsx
```

#### 🟡 无变化案例
```
--- 正在处理: Clinical Trial Results... (MS#: MS2024-002) ---
  - [状态未变] 当前状态与上次记录相同: Under Review
```

#### 🔴 错误处理
```
[失败] 登录失败。请检查用户名、密码或期刊简称。
```

## 🔧 高级功能

### 🔒 临时账户模式

适用于：
- 🎯 偶尔查询其他期刊
- 🔐 不想保存敏感账户信息
- 🧪 测试新期刊配置

选择"[3] 手动输入临时账户"即可使用。

### 📁 自定义数据存储

默认数据存储在 `data/` 文件夹，您可以修改：

```python
# 在 main.py 中找到这行
username_dir = os.path.join('data', account['username'])

# 修改为自定义路径
username_dir = os.path.join('/your/custom/path', account['username'])
```

### 🎨 自定义界面颜色

如果您不喜欢彩色输出：

```bash
# 卸载 colorama
pip uninstall colorama

# 程序会自动降级为纯文本模式
```

## ❓ 常见问题

<details>
<summary><strong>🔐 登录相关问题</strong></summary>

### Q: 登录失败怎么办？
**A**: 检查以下几点：
1. ✅ 用户名密码是否正确
2. ✅ 期刊简称是否正确（区分大小写）
3. ✅ 网络连接是否稳定
4. ✅ 期刊网站是否可以正常访问

### Q: 如何找到正确的期刊简称？
**A**: 
1. 访问期刊的Editorial Manager页面
2. 查看URL，如：`editorialmanager.com/gastro/` → 简称是 `GASTRO`
3. 或者联系期刊编辑部询问

### Q: 支持双因素认证(2FA)吗？
**A**: 目前不支持。如果期刊启用了2FA，建议使用临时账户模式手动处理。

</details>

<details>
<summary><strong>📊 数据和文件问题</strong></summary>

### Q: Excel文件被占用怎么办？
**A**: 程序会自动检测并提示：
```
[操作暂停] 文件 'xxx.xlsx' 正被另一程序占用。
请关闭该Excel文件后，按 Enter键 继续...
```
关闭Excel文件后按Enter即可。

### Q: 如何备份我的追踪数据？
**A**: 直接复制整个 `data/` 文件夹即可。

### Q: 可以修改Excel文件格式吗？
**A**: 可以修改 `main.py` 中的Excel写入部分，或者提交Feature Request。

</details>

<details>
<summary><strong>🛠️ 技术问题</strong></summary>

### Q: 为什么推荐使用虚拟环境？
**A**: 虚拟环境的好处：
- 🔒 隔离项目依赖，避免版本冲突
- 🧹 保持系统Python环境干净  
- 📦 便于项目迁移和分享
- 🛡️ 避免权限问题

### Q: 程序运行很慢怎么办？
**A**: 
1. 检查网络连接速度
2. 尝试修改 `config.py` 中的超时设置
3. 如果稿件很多，属于正常现象

### Q: 支持代理服务器吗？
**A**: 目前不支持，但您可以通过系统代理或修改requests配置实现。

</details>

<details>
<summary><strong>🆕 新功能请求</strong></summary>

### Q: 能否支持其他期刊系统？
**A**: 目前专注于Editorial Manager系统。如有其他需求，请提交Issue讨论。

### Q: 能否添加邮件通知功能？
**A**: 这是一个很好的想法！请在Issues中提交Feature Request。

### Q: 能否支持API接口？
**A**: 期刊网站通常不提供公开API，目前只能通过网页抓取实现。

</details>

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 🌟 如何贡献

1. **🍴 Fork 本项目**
2. **🌿 创建特性分支** (`git checkout -b feature-amazing-feature`)
3. **💾 提交更改** (`git commit -m 'Add some amazing feature'`)
4. **📤 推送到分支** (`git push origin feature-amazing-feature`)
5. **🎯 提交 Pull Request**

### 📝 贡献类型

- 🐛 **Bug 修复** - 发现并修复问题
- ✨ **新功能** - 添加实用的新功能
- 📚 **文档改进** - 完善README和代码注释
- 🎨 **代码优化** - 提升代码质量和性能
- 🧪 **测试覆盖** - 添加单元测试和集成测试

### 🏷️ Issue 标签

- `bug` - 程序错误
- `enhancement` - 功能增强
- `documentation` - 文档相关
- `good first issue` - 适合新手
- `help wanted` - 需要帮助

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源。

```
MIT License

Copyright (c) 2024 em-tracker contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 🙏 致谢

### 💝 特别感谢

- 🔬 **所有使用本工具的研究者们** - 您的反馈让工具变得更好
- 🏥 **医学研究社区** - 为学术进步做出的无私贡献
- 💻 **开源社区** - 提供的优秀工具和库支持

### 🛠️ 技术致谢

本项目使用了以下优秀的开源项目：

- [requests](https://requests.readthedocs.io/) - HTTP 库
- [pandas](https://pandas.pydata.org/) - 数据处理
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - HTML 解析
- [colorama](https://pypi.org/project/colorama/) - 跨平台彩色终端
- [xlsxwriter](https://xlsxwriter.readthedocs.io/) - Excel 文件写入

### 🌟 贡献者

感谢所有为本项目做出贡献的开发者：

<!-- 这里会自动生成贡献者列表 -->
<a href="https://github.com/taozhe6/em-tracker/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=taozhe6/em-tracker" />
</a>

---

<div align="center">

### 🌟 如果这个项目对您有帮助，请给我们一个 Star！

[![Star History Chart](https://api.star-history.com/svg?repos=taozhe6/em-tracker&type=Date)](https://star-history.com/#taozhe6/em-tracker&Date)

**Made with ❤️ for the research community**

[⬆ 回到顶部](#-editorial-manager-tracker)

</div>
