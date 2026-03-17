# 快速开始

本指南将帮助您在 5 分钟内快速接入 TangAPI。

## 前置要求

- 已注册 TangAPI 账户
- 已获取 API Key

## 步骤 1：安装 SDK（可选）

我们提供多种语言的 SDK，您也可以直接使用 HTTP 请求。

### Python

```bash
pip install tangapi-sdk
```

### Node.js

```bash
npm install tangapi-sdk
```

## 步骤 2：配置 API Key

### 方式一：环境变量（推荐）

```bash
export TANGAPI_API_KEY="your_api_key_here"
```

### 方式二：代码中配置

```python
from tangapi import TangAPI

client = TangAPI(api_key="your_api_key_here")
```

## 步骤 3：发送第一请求

### 使用 SDK

```python
from tangapi import TangAPI

client = TangAPI(api_key="your_api_key_here")

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
curl -X POST https://api.tangapi.com/v1/chat/completions \
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
