def get_status_color(value, warn=70, crit=85):
    if value < warn: return "#2ecc71" # Kuma Green
    if value < crit: return "#f1c40f" # Kuma Yellow
    return "#e74c3c" # Kuma Red

def render_svg(metrics: dict) -> str:
    cpu = metrics["cpu"]["percent"]
    ram = metrics["ram"]["percent"]
    temp = metrics["temperature"]["cpu_avg"] or 0
    temp_color = get_status_color(temp, 55, 75)
    uptime = metrics["uptime_human"]

    return f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="460" height="90" viewBox="0 0 460 90">
      <rect width="460" height="90" rx="12" fill="#161b22" stroke="#30363d" stroke-width="1"/>
      
      <circle cx="25" cy="30" r="4" fill="#2ecc71">
        <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite" />
      </circle>
      <text x="40" y="35" fill="#8b949e" font-size="13" font-family="monospace">uptime:</text>
      <text x="95" y="35" fill="#2ecc71" font-size="13" font-family="monospace" font-weight="bold">{uptime}</text>

      <text x="20" y="65" fill="#8b949e" font-size="13" font-family="monospace">🌡 temp:</text>
      <text x="95" y="65" fill="{temp_color}" font-size="13" font-family="monospace" font-weight="bold"> {temp}°C</text>


      <line x1="220" y1="20" x2="220" y2="70" stroke="#30363d" stroke-width="1"/>


      <text x="240" y="35" fill="#8b949e" font-size="13" font-family="monospace">⏲ CPU</text>
      <rect x="290" y="26" width="100" height="10" rx="5" fill="#30363d"/>
      <rect x="290" y="26" width="{max(0, cpu)}" height="10" rx="5" fill="{get_status_color(cpu)}"/>
      <text x="392" y="35" fill="{get_status_color(cpu)}" font-size="12" font-family="monospace">{cpu}%</text>

      <text x="240" y="65" fill="#8b949e" font-size="13" font-family="monospace">⏲ RAM</text>
      <rect x="290" y="56" width="100" height="10" rx="5" fill="#30363d"/>
      <rect x="290" y="56" width="{max(0, ram)}" height="10" rx="5" fill="{get_status_color(ram)}"/>
      <text x="392" y="65" fill="{get_status_color(ram)}" font-size="12" font-family="monospace">{ram}%</text>
    </svg>
    """