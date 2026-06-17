# TangAPI

> 大模型供应服务 API 文档

## 简介

TangAPI 是一个提供大语言模型 API 接入服务的平台，支持多种主流模型接入，为开发者提供稳定、可靠的 AI 能力输出。

## 功能特性

- 🚀 多模型支持 - 兼容 OpenAI、Claude、Gemini 等主流模型
- 💰 计费灵活 - 按量计费，实时消耗统计
- 🔒 安全可靠 - API 密钥管理，企业级安全保障
- 📊 数据分析 - 用量统计，调用日志查看
- ⚡ 快速接入 - 简洁的 API 接口，快速上手

## 快速开始

### 获取 API Key

1. 登录 [TangAPI 控制台](https://tang.092366.xyz)
2. 进入「API 密钥」页面
3. 点击「创建密钥」
4. 复制并妥善保存您的 API Key

### 调用示例

```bash
curl -X POST https://ai.092399.xyz/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你好，请介绍一下自己"}]
  }'
```

## 说明

- 价格与计费请以官方页面为准： [Tang API](https://tang.092366.xyz/pricing)

## 文档目录

- [快速开始](quickstart.md) - 5分钟快速入门
- [API 参考](api-reference.md) - 完整的 API 接口文档
- [价格说明](pricing.md) - 定价和计费方式
- [常见问题](faq.md) - 常见问题解答
