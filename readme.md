# 电负荷预测上位机

## 项目描述

这是一个基于Python和Qt开发的电负荷预测上位机软件，用于实时监测和预测电力负荷数据。通过串口和4G模块获取数据，进行处理和可视化展示。

## 功能特性

- **数据采集**：支持通过串口和4G模块读取电力负荷数据
- **数据处理**：实时处理和分析负荷数据
- **配置管理**：灵活的系统配置选项
- **用户界面**：直观的Qt图形界面
- **数据缓存**：本地数据缓存功能

## 安装说明

### 系统要求

- Python 3.7+
- Windows操作系统

### 依赖项安装

1. 克隆或下载项目到本地
2. 安装Python依赖包：

```bash
pip install -r requirements.txt
```

## 使用方法

1. 运行主程序：

```bash
python main.py
```

2. 在界面中配置串口和GPRS参数
3. 开始数据采集和监控

## 项目结构

- `main.py` - 主程序入口
- `main_window.py` - 主窗口界面
- `data_processor.py` - 数据处理模块
- `serial_reader.py` - 串口数据读取
- `gprs_reader.py` - GPRS数据读取
- `config_manager.py` - 配置管理
- `settings_dialog.py` - 设置对话框
- `ui_form.py` - UI表单定义
- `config.json` - 配置文件
- `energy_cache.json` - 数据缓存文件

## 构建说明

项目使用PyInstaller进行打包：

```bash
pyinstaller 电负荷预测上位机
```

构建后的可执行文件位于`dist/电负荷预测上位机/`目录下。

## 许可证

本项目采用MIT许可证。详见LICENSE文件。

## 贡献

欢迎提交Issue和Pull Request来改进项目。

## 联系方式

如有问题，请通过GitHub Issues联系。
