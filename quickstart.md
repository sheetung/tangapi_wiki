# 快速开始

本指南将帮助您在 5 分钟内快速接入 TangAPI。

## 前置要求

- 已注册 TangAPI 账户
- 已获取 API Key

## 步骤 1：安装 OpenAI SDK

TangAPI 兼容 OpenAI API，您可以直接使用 OpenAI SDK。

### Python

```bash
pip install openai
```

### Node.js

```bash
npm install openai
```

## 步骤 2：配置 API Key

### 方式一：环境变量（推荐）

```bash
export OPENAI_API_KEY="your_tangapi_api_key"
export OPENAI_BASE_URL="https://tang.092366.xyz/v1"
```

### 方式二：代码中配置

```python
from openai import OpenAI

client = OpenAI(
    api_key="your_tangapi_api_key",
    base_url="https://tang.092366.xyz/v1"
)
```

## 步骤 3：发送第一个请求

```python
from openai import OpenAI

client = OpenAI(
    api_key="your_tangapi_api_key",
    base_url="https://tang.092366.xyz/v1"
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "你好，请介绍一下自己"}
    ]
)

print(response.choices[0].message.content)
```

### 使用 cURL

```bash
curl -X POST https://ai.092399.xyz/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你好，请介绍一下自己"}]
  }'
```

## 响应示例

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-4",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "你好！我是 TangAPI 的大模型服务助手..."
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 50,
    "total_tokens": 60
  }
}
```

## 下一步

- 阅读 [API 参考](api-reference.md) 了解更多接口
- 查看 [价格说明](pricing.md) 了解计费详情
