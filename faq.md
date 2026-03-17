# 常见问题

## 账户问题

### Q: 如何注册 TangAPI 账户？
A: 访问 [tangapi.com](https://tangapi.com)，点击「注册」，使用邮箱或手机号完成注册即可。

### Q: API Key 泄露了怎么办？
A: 立即登录控制台，在「API 密钥」页面删除泄露的密钥，并创建新的 API Key。

### Q: 如何修改账户密码？
A: 登录控制台后，进入「账户设置」->「安全设置」修改密码。

---

## 使用问题

### Q: 支持哪些模型？
A: TangAPI 支持 OpenAI、Anthropic (Claude)、Google (Gemini)、Meta (Llama) 等主流大模型。具体支持列表请查看 [API 参考](api-reference.md)。

### Q: 请求超时怎么办？
A: 可以尝试以下方法：
1. 检查网络连接
2. 减少 `max_tokens` 参数
3. 换用响应更快的模型（如 gpt-3.5-turbo）
4. 联系技术支持

### Q: 如何实现流式输出？
A: 在请求中设置 `stream: true`，详细示例请查看 [API 参考](api-reference.md#流式响应)。

### Q: 支持 WebSocket 吗？
A: 目前仅支持 HTTP 流式响应，WebSocket 正在开发中。

---

## 计费问题

### Q: 免费额度用完怎么办？
A: 可以继续使用后付费模式，或购买套餐计划。请及时充值以避免服务中断。

### Q: 可以退款吗？
A: 未使用的余额可以申请退款，请联系客服处理。

### Q: 如何查看账单？
A: 登录控制台，进入「账单」页面查看详细账单记录。

---

## 技术问题

### Q: SDK 支持哪些语言？
A: 目前提供 Python、Node.js、Go、Java SDK。其他语言可使用 REST API。

### Q: 如何处理并发请求？
A: TangAPI 支持高并发，但有速率限制。请参考 [价格说明](pricing.md) 中的速率限制说明。

### Q: 返回的错误信息含义是什么？
A: 请查看 [API 参考](api-reference.md#错误响应) 中的错误代码表。

### Q: 支持代理/内网部署吗？
A: 支持企业版用户申请私有部署，请联系商务洽谈。

---

## 联系我们

- 📧 邮箱：support@tangapi.com
- 💬 微信：扫描控制台二维码
- 📖 文档：https://docs.tangapi.com

如有问题，请随时联系我们！
