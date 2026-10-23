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

```aura width=108 height=32 link="https://www.createbykarla.com" inline align=center
<SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(17,24,39)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='9'/><path d='M3 12h18'/><path d='M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18'/></svg>" text="Portfolio" backgroundColor="#FFFFFF" textColor="#111827" borderColor="#E5E7EB" fontSize={12} iconSize="14" width={108} height={32} gradientStops={[{ offset: '0%', color: '#6FBF00' }, { offset: '25%', color: '#f59e0b' }, { offset: '50%', color: '#D73961' }, { offset: '75%', color: '#A22887' }, { offset: '100%', color: '#00C2AB' }]} />
```
```aura width=108 height=32 link="mailto:karlatovar012@gmail.com" inline align=center
<SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(17,24,39)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><rect x='3' y='5' width='18' height='14' rx='2'/><path d='M3 7l9 6l9-6'/></svg>" text="Email" backgroundColor="#FFFFFF" textColor="#111827" borderColor="#E5E7EB" fontSize={12} iconSize="14" width={108} height={32} gradientStops={[{ offset: '0%', color: '#00C2AB' }, { offset: '25%', color: '#6FBF00' }, { offset: '50%', color: '#f59e0b' }, { offset: '75%', color: '#D73961' }, { offset: '100%', color: '#A22887' }]} />
```
```aura width=108 height=32 link="https://github.com/KarlaTovar-06" inline align=center
<SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(17,24,39)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M8 8l-5 4l5 4'/><path d='M16 8l5 4l-5 4'/></svg>" text="GitHub" backgroundColor="#FFFFFF" textColor="#111827" borderColor="#E5E7EB" fontSize={12} iconSize="14" width={108} height={32} gradientStops={[{ offset: '0%', color: '#A22887' }, { offset: '25%', color: '#00C2AB' }, { offset: '50%', color: '#6FBF00' }, { offset: '75%', color: '#f59e0b' }, { offset: '100%', color: '#D73961' }]} />
```

<p align="center">
  <img src="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/terminal.gif" alt="Terminal" width="760" />
</p>

<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/react"><img src="https://iconic-api.onrender.com/light/react" width="48" alt="React"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/nextjs"><img src="https://iconic-api.onrender.com/light/nextjs" width="48" alt="Next.js"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/typescript"><img src="https://iconic-api.onrender.com/light/typescript" width="48" alt="TypeScript"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/js"><img src="https://iconic-api.onrender.com/light/js" width="48" alt="JavaScript"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/html"><img src="https://iconic-api.onrender.com/light/html" width="48" alt="HTML"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/css"><img src="https://iconic-api.onrender.com/light/css" width="48" alt="CSS"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/tailwind"><img src="https://iconic-api.onrender.com/light/tailwind" width="48" alt="Tailwind"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/python"><img src="https://iconic-api.onrender.com/light/python" width="48" alt="Python"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/php"><img src="https://iconic-api.onrender.com/light/php" width="48" alt="PHP"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/laravel"><img src="https://iconic-api.onrender.com/light/laravel" width="48" alt="Laravel"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/swift"><img src="https://iconic-api.onrender.com/light/swift" width="48" alt="Swift"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/unity"><img src="https://iconic-api.onrender.com/light/unity" width="48" alt="Unity"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/git"><img src="https://iconic-api.onrender.com/light/git" width="48" alt="Git"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://iconic-api.onrender.com/dark/figma"><img src="https://iconic-api.onrender.com/light/figma" width="48" alt="Figma"></picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/snake.svg" />
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/snake.svg" />
  </picture>
</p>