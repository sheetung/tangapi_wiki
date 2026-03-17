# API 参考

本文档详细描述了 TangAPI 的所有 API 接口。

## 基础信息

| 项目 | 说明 |
|------|------|
| 基础 URL | `http://49.233.13.104:3333` |
| 认证方式 | Bearer Token |
| 数据格式 | JSON |
| 编码 | UTF-8 |

## 认证

所有 API 请求需要在 Header 中包含您的 API Key：

```http
Authorization: Bearer YOUR_API_KEY
```

## 错误响应

### 错误响应格式

```json
{
  "error": {
    "code": "invalid_api_key",
    "message": "API 密钥无效或已过期",
    "param": null
  }
}
```

### 错误代码表

| 错误代码 | HTTP 状态码 | 说明 |
|---------|-------------|------|
| invalid_api_key | 401 | API 密钥无效 |
| insufficient_quota | 402 | 账户余额不足 |
| rate_limit_exceeded | 429 | 请求频率超限 |
| server_error | 500 | 服务器内部错误 |
| service_unavailable | 503 | 服务暂不可用 |

---

## Chat Completions

发送对话请求，获取模型生成的回答。

### 请求

```http
POST /v1/chat/completions
```

### 请求体

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| model | string | 是 | 模型名称，如 `gpt-4`、`gpt-3.5-turbo`、`claude-3-opus` |
| messages | array | 是 | 对话消息数组 |
| messages[].role | string | 是 | 角色：`system`、`user`、`assistant` |
| messages[].content | string | 是 | 消息内容 |
| temperature | float | 否 | 采样温度，0-2，默认 1.0 |
| max_tokens | integer | 否 | 最大生成 token 数 |
| top_p | float | 否 | nucleus 采样，0-1，默认 1.0 |
| stream | boolean | 否 | 是否流式返回，默认 false |
| stop | array | 否 | 停止词列表 |
| presence_penalty | float | 否 | 存在惩罚，-2 到 2 |
| frequency_penalty | float | 否 | 频率惩罚，-2 到 2 |

### 请求示例

```bash
curl -X POST http://49.233.13.104:3333/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "system", "content": "你是一个有帮助的助手"},
      {"role": "user", "content": "请介绍一下北京"}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }'
```

### 响应示例

```json
{
  "id": "chatcmpl-abc123xyz",
  "object": "chat.completion",
  "created": 1710672000,
  "model": "gpt-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "北京是中国的首都，位于华北平原北部..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 30,
    "completion_tokens": 120,
    "total_tokens": 150
  }
}
```

### 流式响应

设置 `stream: true` 获取流式响应：

```bash
curl -X POST http://49.233.13.104:3333/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "讲个笑话"}],
    "stream": true
  }'
```

流式响应格式：

```
data: {"id":"chatcmpl-xxx","object":"chat.completion.chunk","created":1710672000,"model":"gpt-4","choices":[{"index":0,"delta":{"content":"这","role":"assistant"},"finish_reason":null}]}

data: {"id":"chatcmpl-xxx","object":"chat.completion.chunk","created":1710672000,"model":"gpt-4","choices":[{"index":0,"delta":{"content":"是"},"role":"assistant"},"finish_reason":null}]}

data: [DONE]
```

---

## 模型列表

获取可用的模型列表。

### 请求

```http
GET /v1/models
```

### 响应示例

```json
{
  "object": "list",
  "data": [
    {
      "id": "gpt-4",
      "object": "model",
      "created": 1687888000,
      "owned_by": "openai"
    },
    {
      "id": "gpt-3.5-turbo",
      "object": "model",
      "created": 1677610600,
      "owned_by": "openai"
    },
    {
      "id": "claude-3-opus",
      "object": "model",
      "created": 1709596800,
      "owned_by": "anthropic"
    }
  ]
}
```

---

## 账户信息

获取账户余额和使用量统计。

### 请求

```http
GET /v1/user/account
```

### 响应示例

```json
{
  "id": "user_abc123",
  "email": "user@example.com",
  "balance": {
    "currency": "USD",
    "amount": 99.50
  },
  "plan": "pro",
  "created_at": 1704067200
}
```

---

## 使用量统计

获取 API 使用量统计。

### 请求

```http
GET /v1/user/usage?start_date=2024-01-01&end_date=2024-01-31
```

### 查询参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| start_date | string | 是 | 开始日期，YYYY-MM-DD |
| end_date | string | 是 | 结束日期，YYYY-MM-DD |

### 响应示例

```json
{
  "object": "usage",
  "start_date": "2024-01-01",
  "end_date": "2024-01-31",
  "usage": [
    {
      "date": "2024-01-01",
      "prompt_tokens": 1000,
      "completion_tokens": 500,
      "total_tokens": 1500,
      "cost": 0.015
    }
  ],
  "total_usage": {
    "prompt_tokens": 30000,
    "completion_tokens": 15000,
    "total_tokens": 45000,
    "cost": 0.45
  }
}
```
