import os
import re

def rebuild_index():
    # 1. Read the full data from resources/어색A서먹I .txt
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'resources', '어색A서먹I .txt')
    print(f"Loading data from: {data_path}")
    
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        return

    with open(data_path, 'r', encoding='utf-8') as f:
        data_content = f.read()

    # Extract the humorData array part (everything between [ and ];)
    match = re.search(r'const humorData = \[(.*?)\];', data_content, re.DOTALL)
    if match:
        humor_data_js = match.group(1).strip()
    else:
        # Fallback if the format is slightly different
        clean_data = data_content.replace('const humorData = [', '').replace('];', '').strip()
        humor_data_js = clean_data

    count = humor_data_js.count('situation:')

    # 2. Define the Ultra-Premium High-End HTML Template
    html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>어색A 서먹I | Premium AI Social Guide</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    
    <style>
        :root {
            --primary: #818cf8;
            --secondary: #c084fc;
            --accent: #22d3ee;
            --success: #34d399;
            --bg-deep: #020617;
            --glass: rgba(15, 23, 42, 0.7);
            --glass-border: rgba(255, 255, 255, 0.12);
            --text-main: #f8fafc;
            --text-dim: #94a3b8;
            --neon-glow: 0 0 15px rgba(129, 140, 248, 0.4);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Outfit', 'Inter', sans-serif; -webkit-tap-highlight-color: transparent; }
        
        body { 
            background: var(--bg-deep); 
            color: var(--text-main); 
            min-height: 100vh; 
            overflow: hidden;
            display: flex; align-items: center; justify-content: center;
        }

        /* [Dynamic Background] */
        .bg-canvas {
            position: fixed; inset: 0; z-index: -1;
            background: radial-gradient(circle at 10% 20%, #1e1b4b 0%, transparent 40%),
                        radial-gradient(circle at 90% 80%, #312e81 0%, transparent 40%),
                        radial-gradient(circle at 50% 50%, #020617 0%, #000 100%);
        }

        .floating-orb {
            position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.12;
            animation: float 25s infinite alternate ease-in-out;
        }
        .orb-1 { width: 400px; height: 400px; background: var(--primary); top: -100px; left: -100px; }
        .orb-2 { width: 350px; height: 350px; background: var(--secondary); bottom: -50px; right: -50px; animation-delay: -5s; }
        .orb-3 { width: 300px; height: 300px; background: var(--accent); top: 50%; left: 50%; animation-delay: -10s; }

        @keyframes float {
            0% { transform: translate(0, 0) scale(1); }
            100% { transform: translate(150px, 80px) scale(1.3); }
        }

        /* [Gateway: AI Vision Scan] */
        #smileGateway {
            position: fixed; inset: 0; z-index: 9999;
            background: rgba(2, 6, 23, 0.9);
            backdrop-filter: blur(50px);
            display: none;
            flex-direction: column; align-items: center; justify-content: center;
            padding: 24px; text-align: center;
            transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .auth-card {
            width: 100%; max-width: 420px;
            padding: 48px 32px; border-radius: 48px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.6);
            transform: translateY(0);
            animation: cardIn 1s cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        @keyframes cardIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .scanner-container {
            position: relative; width: 240px; height: 240px;
            margin: 32px auto; border-radius: 32px; overflow: hidden;
            border: 2px solid var(--glass-border);
            background: #000;
        }

        #webcam { width: 100%; height: 100%; object-fit: cover; transform: scaleX(-1); }
        
        .scan-line {
            position: absolute; top: 0; left: 0; width: 100%; height: 2px;
            background: var(--accent); box-shadow: 0 0 15px var(--accent);
            animation: scan 2.5s infinite linear;
            z-index: 10;
        }
        @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }

        .loader {
            width: 48px; height: 48px; border: 3px solid rgba(255,255,255,0.1);
            border-top: 3px solid var(--primary); border-radius: 50%;
            animation: spin 1s linear infinite; margin: 20px auto;
        }
        @keyframes spin { 100% { transform: rotate(360deg); } }

        /* [App Shell] */
        .app-shell {
            width: 100%; max-width: 500px; height: 100vh;
            display: none; flex-direction: column;
            background: transparent;
            opacity: 0; transition: opacity 0.6s ease;
        }
        .app-shell.active { opacity: 1; display: flex; }

        .header {
            padding: 40px 24px 20px; text-align: center;
        }
        .logo {
            font-size: 2rem; font-weight: 800; letter-spacing: -1px;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            filter: drop-shadow(var(--neon-glow));
        }

        .content-area {
            flex: 1; overflow-y: auto; padding: 0 24px 100px;
            scrollbar-width: none;
        }
        .content-area::-webkit-scrollbar { display: none; }

        /* [Components] */
        .premium-card {
            background: var(--glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 32px; padding: 32px;
            margin-bottom: 24px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .balance-game {
            background: linear-gradient(135deg, rgba(129, 140, 248, 0.1), rgba(192, 132, 252, 0.1));
            border: 1px solid rgba(129, 140, 248, 0.2);
            text-align: center;
        }
        .balance-title { font-size: 0.85rem; color: var(--accent); font-weight: 700; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px; }
        .balance-text { font-size: 1.25rem; font-weight: 600; line-height: 1.4; color: #fff; }

        .nav-grid { display: grid; grid-template-columns: 1fr; gap: 16px; }

        .action-btn {
            position: relative; overflow: hidden;
            padding: 24px; border-radius: 24px; border: none;
            cursor: pointer; display: flex; flex-direction: column;
            align-items: center; justify-content: center; gap: 8px;
            transition: all 0.3s ease; text-align: center;
        }
        .action-btn:active { transform: scale(0.96); }
        
        .btn-purple { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4); }
        .btn-cyan { background: linear-gradient(135deg, #06b6d4, #3b82f6); color: white; box-shadow: 0 10px 20px -5px rgba(6, 182, 212, 0.4); }

        .btn-title { font-size: 1.2rem; font-weight: 800; }
        .btn-desc { font-size: 0.8rem; opacity: 0.8; font-weight: 400; }

        /* [List View] */
        .list-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--glass-border);
            border-radius: 20px; padding: 20px; margin-bottom: 12px;
            cursor: pointer; transition: all 0.2s ease;
            display: flex; align-items: center; justify-content: space-between;
        }
        .list-item:hover { background: rgba(255, 255, 255, 0.08); transform: translateX(5px); }
        .list-item:active { transform: scale(0.98); }

        /* [Result View] */
        .result-view { text-align: center; animation: fadeIn 0.5s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .tag {
            display: inline-block; padding: 8px 16px; border-radius: 100px;
            background: rgba(34, 211, 238, 0.1); color: var(--accent);
            font-size: 0.8rem; font-weight: 700; margin-bottom: 24px;
            border: 1px solid rgba(34, 211, 238, 0.2);
        }

        .guide-box {
            font-size: 1.3rem; font-weight: 600; line-height: 1.5;
            color: #fff; margin-bottom: 32px;
        }

        .joke-bubble {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 24px; padding: 24px;
            font-style: italic; color: var(--text-dim);
            position: relative; margin-bottom: 40px;
        }
        .joke-bubble::after {
            content: '“'; position: absolute; top: -10px; left: 20px;
            font-size: 4rem; opacity: 0.1; font-family: serif;
        }

        .back-btn {
            width: 100%; padding: 18px; border-radius: 18px;
            border: 1px solid var(--glass-border); background: var(--glass);
            color: #fff; font-weight: 600; cursor: pointer;
            transition: all 0.2s ease;
        }
        .back-btn:hover { background: rgba(255, 255, 255, 0.1); }

        /* [Utils] */
        .hide { display: none !important; }
    </style>
</head>
<body>
    <div class="bg-canvas">
        <div class="floating-orb orb-1"></div>
        <div class="floating-orb orb-2"></div>
        <div class="floating-orb orb-3"></div>
    </div>

    <!-- [Gateway] -->
    <div id="smileGateway">
        <div class="auth-card">
            <h2 style="font-weight: 800; font-size: 1.8rem; letter-spacing: -1px;">AI Vision Access</h2>
            <p style="color: var(--text-dim); margin-top: 8px; font-size: 0.95rem;">프리미엄 가이드 입장을 위해<br>환한 미소로 본인을 인증해주세요.</p>
            
            <div class="scanner-container">
                <video id="webcam" autoplay playsinline></video>
                <div class="scan-line"></div>
                <div id="authLoader" class="loader"></div>
            </div>

            <p id="authStatus" style="font-weight: 600; color: var(--accent); margin-bottom: 24px;">AI 시스템을 최적화 중...</p>
            
            <button id="startAuthBtn" class="action-btn btn-purple" style="display:none; width: 100%;">
                <span class="btn-title">카메라 연결하기</span>
            </button>
            
            <button onclick="unlockApp()" style="margin-top: 24px; background: none; border: none; color: var(--text-dim); font-size: 0.85rem; cursor: pointer; text-decoration: underline;">
                인증 없이 입장하기
            </button>
        </div>
    </div>

    <!-- [Main App] -->
    <div id="appShell" class="app-shell">
        <div class="header">
            <div class="logo">어색A 서먹I</div>
        </div>

        <div class="content-area">
            <!-- Home -->
            <div id="homeView">
                <div class="premium-card balance-game">
                    <div class="balance-title">💡 오늘의 밸런스 토크</div>
                    <div id="balanceContent" class="balance-text">불러오는 중...</div>
                </div>

                <div class="nav-grid">
                    <button class="action-btn btn-purple" onclick="showList('어색')">
                        <span class="btn-title">어색AI 가이드</span>
                        <span class="btn-desc">돌발상황 / 민망한 순간 / 실수 대처</span>
                    </button>
                    <button class="action-btn btn-cyan" onclick="showList('서먹')">
                        <span class="btn-title">서먹AI 가이드</span>
                        <span class="btn-desc">초면 대화 / 정적 깨기 / 친밀도 업</span>
                    </button>
                    
                    <button onclick="resetAuth()" style="margin-top:40px; background:none; border:none; color:var(--text-dim); font-size:0.75rem; cursor:pointer; opacity: 0.5;">
                        Authentication Reset (Debug)
                    </button>
                </div>
            </div>

            <!-- List -->
            <div id="listView" class="hide">
                <div id="listItems"></div>
                <button class="back-btn" onclick="showHome()" style="margin-top:20px;">메인으로 돌아가기</button>
            </div>

            <!-- Result -->
            <div id="resultView" class="hide result-view">
                <span id="resTag" class="tag"></span>
                <div id="resGuide" class="guide-box"></div>
                <div id="resJoke" class="joke-bubble"></div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <button class="back-btn" onclick="showList(currentCategory)">목록으로</button>
                    <button class="back-btn" style="background:var(--primary); border:none;" onclick="showHome()">홈으로</button>
                </div>
                <button class="back-btn" style="margin-top:16px; background:rgba(255,255,255,0.05); border:1px dashed var(--accent); color:var(--accent);" onclick="copyResult()">내용 복사하기</button>
            </div>
        </div>
    </div>

    <script type="module">
        // Import MediaPipe from CDN
        import {
            FaceLandmarker,
            FilesetResolver
        } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.3";

        const humorData = [
            {{DATA}}
        ];

        const balanceGames = [
            "평생 양치 안 하기 vs 평생 샤워 안 하기",
            "과거로 가서 비트코인 사기 vs 미래로 가서 로또 번호 알아오기",
            "평생 여름만 있기 vs 평생 겨울만 있기",
            "100% 확률로 1억 받기 vs 10% 확률로 100억 받기",
            "평생 라면만 먹기 vs 평생 치킨만 먹기",
            "아무도 없는 곳에서 투명인간 vs 모두가 쳐다보는 슈퍼스타"
        ];

        const gateway = document.getElementById('smileGateway');
        const shell = document.getElementById('appShell');
        const video = document.getElementById('webcam');
        const authStatus = document.getElementById('authStatus');
        const startAuthBtn = document.getElementById('startAuthBtn');
        const authLoader = document.getElementById('authLoader');

        let faceLandmarker, stream, isUnlocked = false, animReq;

        window.onload = async () => {
            renderBalance();
            if (localStorage.getItem('isUnlocked_v4') === 'true') {
                launchApp();
            } else {
                gateway.style.display = 'flex';
                initAI();
            }
        };

        async function initAI() {
            try {
                const vision = await FilesetResolver.forVisionTasks(
                    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.3/wasm"
                );
                faceLandmarker = await FaceLandmarker.createFromOptions(vision, {
                    baseOptions: {
                        modelAssetPath: "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task",
                        delegate: "GPU"
                    },
                    outputFaceBlendshapes: true,
                    runningMode: "VIDEO"
                });
                authLoader.classList.add('hide');
                authStatus.innerText = "시스템 준비 완료! 웃어주세요.";
                startAuthBtn.style.display = 'flex';
            } catch (e) {
                console.error("AI Init Error:", e);
                authStatus.innerText = "AI 로딩 지연. 수동 입장 가능.";
                startAuthBtn.innerHTML = '<span class="btn-title">바로 입장하기</span>';
                startAuthBtn.style.display = 'flex';
            }
        }

        startAuthBtn.onclick = async () => {
            if (!faceLandmarker) { unlockApp(); return; }
            
            if (startAuthBtn.innerText.includes("입장하기")) { unlockApp(); return; }

            // [Security Check]
            if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
                alert("카메라에 접근할 수 없는 환경입니다.\\n(HTTPS 연결 또는 localhost 접속이 필요합니다)");
                unlockApp();
                return;
            }

            startAuthBtn.style.display = 'none';
            authStatus.innerText = "카메라를 연결하는 중...";
            try {
                stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } });
                video.srcObject = stream;
                
                // Fix race condition: check if metadata is already loaded
                const startPredict = () => {
                    authStatus.innerText = "환하게 웃어보세요! 😊";
                    predict();
                };

                if (video.readyState >= 2) {
                    startPredict();
                } else {
                    video.onloadedmetadata = startPredict;
                }
            } catch (e) {
                console.error("Camera Error:", e);
                alert("카메라를 켤 수 없습니다. 권한 설정을 확인해주세요.");
                unlockApp();
            }
        };

        async function predict() {
            if (isUnlocked) return;
            const now = performance.now();
            try {
                const res = faceLandmarker.detectForVideo(video, now);
                if (res.faceBlendshapes?.length > 0) {
                    const shapes = res.faceBlendshapes[0].categories;
                    const smileL = shapes.find(s => s.categoryName === "mouthSmileLeft").score;
                    const smileR = shapes.find(s => s.categoryName === "mouthSmileRight").score;
                    const smile = (smileL + smileR) / 2;
                    
                    if (smile > 0.45) {
                        confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 }, colors: ['#818cf8', '#c084fc', '#22d3ee'] });
                        authStatus.innerText = "미소 감지 성공! 환영합니다.";
                        setTimeout(unlockApp, 1000);
                        return;
                    }
                }
            } catch (e) {}
            animReq = requestAnimationFrame(predict);
        }

        window.unlockApp = function() {
            isUnlocked = true;
            localStorage.setItem('isUnlocked_v4', 'true');
            if (stream) stream.getTracks().forEach(t => t.stop());
            if (animReq) cancelAnimationFrame(animReq);
            
            gateway.style.opacity = '0';
            setTimeout(() => {
                gateway.style.display = 'none';
                launchApp();
            }, 800);
        }

        function launchApp() {
            gateway.style.display = 'none';
            shell.classList.add('active');
            shell.style.display = 'flex';
        }

        window.resetAuth = function() {
            localStorage.removeItem('isUnlocked_v4');
            location.reload();
        }

        // Navigation
        const views = { 
            home: document.getElementById('homeView'), 
            list: document.getElementById('listView'), 
            result: document.getElementById('resultView') 
        };
        let currentCategory = '';

        function switchView(id) {
            Object.values(views).forEach(v => v.classList.add('hide'));
            views[id].classList.remove('hide');
            document.querySelector('.content-area').scrollTop = 0;
        }

        window.showHome = () => switchView('home');

        window.showList = (cat) => {
            currentCategory = cat;
            const container = document.getElementById('listItems');
            container.innerHTML = `<h3 style="margin-bottom:20px; font-weight:800; color:var(--primary);">${cat === '어색' ? '💦 어색한 상황 대처법' : '🧊 서먹한 관계 깨기'}</h3>`;
            
            humorData.filter(d => d.category === cat).forEach(item => {
                const div = document.createElement('div');
                div.className = 'list-item';
                div.innerHTML = `<span>${item.situation}</span> <span style="opacity:0.3">→</span>`;
                div.onclick = () => showResult(item);
                container.appendChild(div);
            });
            switchView('list');
        };

        function showResult(item) {
            document.getElementById('resTag').innerText = item.category === '어색' ? '돌발/민망 상황' : '초면/서먹 관계';
            document.getElementById('resGuide').innerText = item.guide;
            document.getElementById('resJoke').innerText = item.joke;
            switchView('result');
        }

        window.copyResult = function() {
            const guide = document.getElementById('resGuide').innerText;
            const joke = document.getElementById('resJoke').innerText;
            const text = `[어색A 서먹I 가이드]\n\n💡 대처법: ${guide}\n💬 멘트 추천: "${joke}"`;
            
            navigator.clipboard.writeText(text).then(() => {
                alert('가이드 내용이 복사되었습니다!');
            });
        }

        function renderBalance() {
            const game = balanceGames[Math.floor(Math.random() * balanceGames.length)];
            document.getElementById('balanceContent').innerText = game;
        }
    </script>

</body>
</html>"""

    # 3. Replace placeholders
    final_html = html_template.replace("{{DATA}}", humor_data_js)
    
    # 4. Write the final index.html to both locations
    output_paths = [
        os.path.join(base_dir, 'resources', 'index.html'),
        os.path.join(base_dir, 'index.html')
    ]
    
    for path in output_paths:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(final_html)
    
    print(f"Success: Rebuilt index.html in {len(output_paths)} locations.")

if __name__ == "__main__":
    rebuild_index()
