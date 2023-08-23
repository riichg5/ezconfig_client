# EZConfig 客户端程序

## 使用方法

设置环境变量

| 环境变量 | 说明 |
| --- | --- |
| EZCONFIG_ENV | 环境变量，可选值：DEV、TEST、PROD |
| EZCONFIG_APPID | 应用ID |
| EZCONFIG_SECRET | 应用密钥 |
| EZCONFIG_HOST | EZConfig服务地址 |

**测试参考代码**

EZCONFIG_ENV=DEV EZCONFIG_APPID=xxx.xx.xxx EZCONFIG_SECRET=xxxxxxx EZCONFIG_HOST=https://xxxx.xx python test/test.py
