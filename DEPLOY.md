# 免费部署指南（Vercel + Render）

本文档帮助你把这个项目以**完全免费、不需要信用卡**的方式部署上线。

- **前端**：Vercel（静态托管，全球 CDN，永久免费）
- **后端**：Render Free（FastAPI + WebSocket，免费 750 小时/月）
- **API Key 模式**：终端用户访问页面时，自己在右上角齿轮图标里填写 OpenAI / Anthropic / Gemini 的 key —— 你不需要承担任何调用费用

> ⚠️ Render 免费 tier 的限制：服务 15 分钟无请求会休眠，下次访问要冷启动 ~30 秒。这是免费的代价。

---

## 第 0 步：把代码推到你自己的 GitHub 仓库

当前 `origin` 指向 `abi/screenshot-to-code`（原作者），你没有 push 权限。需要换成你自己的仓库。

### 方式 A：在 GitHub 网页 fork（推荐）

1. 打开 https://github.com/abi/screenshot-to-code
2. 右上角点 **Fork**，选你的账号
3. 在本地把远端切换到你的 fork：

   ```bash
   cd /Users/lyuyixiao/Desktop/screenshot-to-code
   git remote set-url origin https://github.com/<你的用户名>/screenshot-to-code.git
   git add backend/Dockerfile render.yaml frontend/vercel.json frontend/.env.production.example DEPLOY.md
   git commit -m "chore: add free deployment config (Render + Vercel)"
   git push origin main
   ```

### 方式 B：新建一个空仓库

在 GitHub 创建一个空仓库（比如叫 `screenshot-to-code-deploy`），然后：

```bash
cd /Users/lyuyixiao/Desktop/screenshot-to-code
git remote set-url origin https://github.com/<你的用户名>/screenshot-to-code-deploy.git
git push -u origin main
```

---

## 第 1 步：部署后端到 Render（约 5 分钟）

1. 打开 https://render.com/ 用 GitHub 账号登录（首次会要求授权）
2. 顶部菜单进入 **Blueprints** → 点击 **New Blueprint Instance**
   - 直链：https://dashboard.render.com/blueprints
3. 选择刚刚 fork 的 `screenshot-to-code` 仓库
4. Render 会自动读取根目录的 [`render.yaml`](render.yaml)，识别出一个 web service
5. 给 Blueprint 起个名字（比如 `screenshot-to-code`），点 **Apply**
6. 等待首次构建完成（~5-10 分钟，含 Docker 镜像构建）
7. 部署完成后在服务详情页能看到形如 `https://screenshot-to-code-backend-xxxx.onrender.com` 的 URL，**复制下来**，下一步要用

> 💡 第一次访问该 URL 应该能看到一个简单的欢迎页（[`backend/routes/home.py`](backend/routes/home.py) 提供）。

---

## 第 2 步：部署前端到 Vercel（约 3 分钟）

1. 打开 https://vercel.com/ 用 GitHub 账号登录
2. 主页点 **Add New** → **Project**
3. 选择刚刚 fork 的仓库
4. **Root Directory** 一栏点 **Edit**，改为 `frontend`（必须！否则 Vercel 会在仓库根目录找不到 package.json）
5. Framework 应该自动识别为 **Vite**，保持默认即可
6. 展开 **Environment Variables**，添加 2 条（**注意是 https / wss，不是 http / ws**）：

   | Key | Value |
   |---|---|
   | `VITE_HTTP_BACKEND_URL` | `https://你的-render-后端域名.onrender.com` |
   | `VITE_WS_BACKEND_URL` | `wss://你的-render-后端域名.onrender.com` |

7. 点 **Deploy**，等 1-2 分钟
8. 部署完成后获得形如 `https://screenshot-to-code-xxxx.vercel.app` 的 URL —— **这就是你的线上地址**

---

## 第 3 步：验证

1. 浏览器打开 Vercel 给的前端地址
2. 右上角点齿轮图标 ⚙️ ，填入你（或访问者）的 OpenAI / Anthropic / Gemini key
3. 上传一张截图试试，应该能正常生成代码

---

## 常见问题

### Render 构建失败：`ERROR: failed to fetch ...`
通常是网络瞬时问题，去服务详情页点 **Manual Deploy** → **Deploy latest commit** 重试。

### 前端访问后端报 `ws://` 错误或 CORS 错误
- 确认 Vercel 环境变量用的是 `wss://` 而非 `ws://`（https 页面无法连接 ws://）
- 后端 [`backend/main.py`](backend/main.py) 的 CORS 已经配置 `allow_origins=["*"]`，理论上不会报 CORS 错

### 修改环境变量后没生效
Vercel 改完环境变量需要 **Redeploy** 才会生效：项目页 → Deployments → 最新一条 → 三点菜单 → Redeploy。

### Render 总是冷启动很慢
有两个选项：
1. 升级到 Render Starter（$7/月，不休眠）
2. 用 https://uptimerobot.com/ 之类的服务每 10 分钟 ping 一次后端 URL，让它别睡 —— 严格说有违 Render 免费政策，长期不推荐

### 想换平台？
- **后端换 Fly.io**：免休眠、性能更好，但需要绑信用卡（不收费）。指令参考：`fly launch --dockerfile backend/Dockerfile`
- **后端换 Hugging Face Space**：完全免费免信用卡，新建一个 Docker Space，把 [`backend/Dockerfile`](backend/Dockerfile) 内容传上去即可。注意 HF Space 的 WebSocket 偶有不稳

---

## 后续更新

只要 push 到你的 fork 的 `main` 分支：
- Vercel 自动重新构建前端
- Render 自动重新构建后端

无需任何额外操作。
