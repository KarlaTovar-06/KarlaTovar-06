```aura width=800 height=200
<div style={{ display: 'flex', width: '100%', height: '100%', position: 'relative', backgroundColor: '#FFFFFF', borderRadius: 24, overflow: 'hidden', border: '1px solid #E5E7EB' }}>
  <svg width="800" height="200" viewBox="0 0 800 200" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="glowCyan" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="#00C2AB" stopOpacity="0.38" />
        <stop offset="100%" stopColor="#00C2AB" stopOpacity="0" />
      </radialGradient>
      <radialGradient id="glowRosa" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="#D73961" stopOpacity="0.30" />
        <stop offset="100%" stopColor="#D73961" stopOpacity="0" />
      </radialGradient>
      <radialGradient id="glowAmarillo" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="#f59e0b" stopOpacity="0.32" />
        <stop offset="100%" stopColor="#f59e0b" stopOpacity="0" />
      </radialGradient>
      <radialGradient id="glowMorado" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="#A22887" stopOpacity="0.26" />
        <stop offset="100%" stopColor="#A22887" stopOpacity="0" />
      </radialGradient>
      <radialGradient id="glowVerde" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="#6FBF00" stopOpacity="0.28" />
        <stop offset="100%" stopColor="#6FBF00" stopOpacity="0" />
      </radialGradient>
    </defs>
    <style>{`
      @keyframes driftA { 0% { transform: translate(0px, 0px); } 50% { transform: translate(-36px, 16px); } 100% { transform: translate(0px, 0px); } }
      @keyframes driftB { 0% { transform: translate(0px, 0px); } 50% { transform: translate(28px, -14px); } 100% { transform: translate(0px, 0px); } }
      @keyframes driftC { 0% { transform: translate(0px, 0px); } 50% { transform: translate(-22px, -18px); } 100% { transform: translate(0px, 0px); } }
      #orbCyan { animation: driftA 9s ease-in-out infinite; }
      #orbRosa { animation: driftB 11s ease-in-out infinite; }
      #orbAmarillo { animation: driftC 10s ease-in-out infinite; }
      #orbMorado { animation: driftA 12s ease-in-out infinite; }
      #orbVerde { animation: driftB 13s ease-in-out infinite; }
      @media (prefers-color-scheme: dark) {
        path[fill="#FFFFFF"] { fill: #0D1117; }
        [stroke="#E5E7EB"] { stroke: #30363D; }
        path[fill="#111827"] { fill: #F0F6FC; }
        path[fill="#A22887"] { fill: #E56CC4; }
        path[fill="#6B7280"] { fill: #8B949E; }
      }
    `}</style>
    <ellipse id="orbCyan" cx="660" cy="40" rx="190" ry="120" fill="url(#glowCyan)" />
    <ellipse id="orbRosa" cx="540" cy="190" rx="170" ry="100" fill="url(#glowRosa)" />
    <ellipse id="orbAmarillo" cx="770" cy="170" rx="130" ry="90" fill="url(#glowAmarillo)" />
    <ellipse id="orbMorado" cx="430" cy="20" rx="140" ry="80" fill="url(#glowMorado)" />
    <ellipse id="orbVerde" cx="700" cy="110" rx="110" ry="70" fill="url(#glowVerde)" />
  </svg>
  <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', padding: '0 56px' }}>
    <div style={{ display: 'flex', fontSize: 56, fontWeight: 700, color: '#111827', letterSpacing: -1.5 }}>Karla Tovar</div>
    <div style={{ display: 'flex', fontSize: 22, color: '#A22887', marginTop: 8 }}>Software Engineer · Frontend</div>
    <div style={{ display: 'flex', fontSize: 16, color: '#6B7280', marginTop: 6 }}>Mexico City</div>
  </div>
</div>
```
 
```aura width=116 height=32 link="https://www.createbykarla.com" inline
<div style={{ display: 'flex', width: '100%', height: '100%', paddingRight: 8 }}>
  <style>{`
    @media (prefers-color-scheme: dark) {
      path[fill="#FFFFFF"] { fill: #161B22; }
      path[fill="#111827"] { fill: #F0F6FC; }
    }
  `}</style>
  <SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162,40,135)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='9'/><path d='M3 12h18'/><path d='M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18'/></svg>" text="Portfolio" backgroundColor="#FFFFFF" textColor="#111827" borderColor="#A22887" fontSize={12} iconSize="14" width={108} height={32} gradientStops={[{ offset: '0%', color: '#A22887' }, { offset: '100%', color: '#A22887' }]} />
</div>
```
```aura width=116 height=32 link="mailto:karlatovar012@gmail.com" inline
<div style={{ display: 'flex', width: '100%', height: '100%', paddingRight: 8 }}>
  <style>{`
    @media (prefers-color-scheme: dark) {
      path[fill="#FFFFFF"] { fill: #161B22; }
      path[fill="#111827"] { fill: #F0F6FC; }
    }
  `}</style>
  <SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(0,194,171)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><rect x='3' y='5' width='18' height='14' rx='2'/><path d='M3 7l9 6l9-6'/></svg>" text="Email" backgroundColor="#FFFFFF" textColor="#111827" borderColor="#00C2AB" fontSize={12} iconSize="14" width={108} height={32} gradientStops={[{ offset: '0%', color: '#00C2AB' }, { offset: '100%', color: '#00C2AB' }]} />
</div>
```
```aura width=116 height=32 link="https://github.com/KarlaTovar-06" inline
<div style={{ display: 'flex', width: '100%', height: '100%', paddingRight: 8 }}>
  <style>{`
    @media (prefers-color-scheme: dark) {
      path[fill="#FFFFFF"] { fill: #161B22; }
      path[fill="#111827"] { fill: #F0F6FC; }
    }
  `}</style>
  <SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(215,57,97)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M8 8l-5 4l5 4'/><path d='M16 8l5 4l-5 4'/></svg>" text="GitHub" backgroundColor="#FFFFFF" textColor="#111827" borderColor="#D73961" fontSize={12} iconSize="14" width={108} height={32} gradientStops={[{ offset: '0%', color: '#D73961' }, { offset: '100%', color: '#D73961' }]} />
</div>
```

### About

Software engineer focused on frontend, with a product mindset. I build thoughtful digital experiences with React, Next.js and TypeScript, and enjoy turning technical ideas into real products.

<img src="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/terminal-light.gif#gh-light-mode-only" alt="Terminal" width="760"><img src="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/terminal-dark.gif#gh-dark-mode-only" alt="Terminal" width="760">

### Stack

<img src="https://iconic-api.onrender.com/light/react#gh-light-mode-only" width="44" alt="React"><img src="https://iconic-api.onrender.com/dark/react#gh-dark-mode-only" width="44" alt="React">
<img src="https://iconic-api.onrender.com/light/nextjs#gh-light-mode-only" width="44" alt="Next.js"><img src="https://iconic-api.onrender.com/dark/nextjs#gh-dark-mode-only" width="44" alt="Next.js">
<img src="https://iconic-api.onrender.com/light/typescript#gh-light-mode-only" width="44" alt="TypeScript"><img src="https://iconic-api.onrender.com/dark/typescript#gh-dark-mode-only" width="44" alt="TypeScript">
<img src="https://iconic-api.onrender.com/light/js#gh-light-mode-only" width="44" alt="JavaScript"><img src="https://iconic-api.onrender.com/dark/js#gh-dark-mode-only" width="44" alt="JavaScript">
<img src="https://iconic-api.onrender.com/light/html#gh-light-mode-only" width="44" alt="HTML"><img src="https://iconic-api.onrender.com/dark/html#gh-dark-mode-only" width="44" alt="HTML">
<img src="https://iconic-api.onrender.com/light/css#gh-light-mode-only" width="44" alt="CSS"><img src="https://iconic-api.onrender.com/dark/css#gh-dark-mode-only" width="44" alt="CSS">
<img src="https://iconic-api.onrender.com/light/tailwind#gh-light-mode-only" width="44" alt="Tailwind"><img src="https://iconic-api.onrender.com/dark/tailwind#gh-dark-mode-only" width="44" alt="Tailwind">
<img src="https://iconic-api.onrender.com/light/python#gh-light-mode-only" width="44" alt="Python"><img src="https://iconic-api.onrender.com/dark/python#gh-dark-mode-only" width="44" alt="Python">
<img src="https://iconic-api.onrender.com/light/php#gh-light-mode-only" width="44" alt="PHP"><img src="https://iconic-api.onrender.com/dark/php#gh-dark-mode-only" width="44" alt="PHP">
<img src="https://iconic-api.onrender.com/light/laravel#gh-light-mode-only" width="44" alt="Laravel"><img src="https://iconic-api.onrender.com/dark/laravel#gh-dark-mode-only" width="44" alt="Laravel">
<img src="https://iconic-api.onrender.com/light/swift#gh-light-mode-only" width="44" alt="Swift"><img src="https://iconic-api.onrender.com/dark/swift#gh-dark-mode-only" width="44" alt="Swift">
<img src="https://iconic-api.onrender.com/light/unity#gh-light-mode-only" width="44" alt="Unity"><img src="https://iconic-api.onrender.com/dark/unity#gh-dark-mode-only" width="44" alt="Unity">
<img src="https://iconic-api.onrender.com/light/git#gh-light-mode-only" width="44" alt="Git"><img src="https://iconic-api.onrender.com/dark/git#gh-dark-mode-only" width="44" alt="Git">
<img src="https://iconic-api.onrender.com/light/figma#gh-light-mode-only" width="44" alt="Figma"><img src="https://iconic-api.onrender.com/dark/figma#gh-dark-mode-only" width="44" alt="Figma">

### GitHub

<p align="center">
  <img height="165" alt="General stats" src="https://github-readme-stats.vercel.app/api?username=KarlaTovar-06&show_icons=true&hide_border=true&rank_icon=github&theme=transparent&title_color=A22887&icon_color=00C2AB&text_color=374151#gh-light-mode-only" /><img height="165" alt="General stats" src="https://github-readme-stats.vercel.app/api?username=KarlaTovar-06&show_icons=true&hide_border=true&rank_icon=github&theme=transparent&title_color=E56CC4&icon_color=00C2AB&text_color=C9D1D9#gh-dark-mode-only" />
  <img height="165" alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KarlaTovar-06&layout=compact&hide_border=true&theme=transparent&title_color=A22887&text_color=374151#gh-light-mode-only" /><img height="165" alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KarlaTovar-06&layout=compact&hide_border=true&theme=transparent&title_color=E56CC4&text_color=C9D1D9#gh-dark-mode-only" />
</p>

<p align="center">
  <img alt="Streak stats" src="https://streak-stats.demolab.com?user=KarlaTovar-06&hide_border=true&theme=transparent&ring=A22887&fire=D73961&currStreakNum=111827&sideNums=111827&currStreakLabel=A22887&sideLabels=6B7280&dates=6B7280&stroke=E5E7EB#gh-light-mode-only" /><img alt="Streak stats" src="https://streak-stats.demolab.com?user=KarlaTovar-06&hide_border=true&theme=transparent&ring=E56CC4&fire=D73961&currStreakNum=F0F6FC&sideNums=F0F6FC&currStreakLabel=E56CC4&sideLabels=8B949E&dates=8B949E&stroke=30363D#gh-dark-mode-only" />
</p>

### Activity

<img alt="Contribution snake" src="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/snake.svg#gh-light-mode-only"><img alt="Contribution snake" src="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/snake-dark.svg#gh-dark-mode-only">
