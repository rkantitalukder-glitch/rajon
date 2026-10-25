#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║   FB Account Registration & GraphQL Filter Tool v4.5 PRO     ║
║   DEV:     @O_J_A_N_T_H_A                                    ║
╚══════════════════════════════════════════════════════════════╝

Usage:
  python fb_reg.py
"""

import os, sys, re, json, uuid, time, random, string, base64
import threading, itertools
from concurrent.futures import ThreadPoolExecutor

if sys.platform == "win32":
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass
    os.system('')

try:
    from curl_cffi import requests
except ImportError:
    print("[!] curl_cffi not installed. Run: pip install curl-cffi cryptography")
    sys.exit(1)

try:
    import telebot
    from telebot import types
except ImportError:
    print("[!] pyTelegramBotAPI not installed. Run: pip install pyTelegramBotAPI")
    sys.exit(1)

# ═══════════════════════════════════════════════════════
#  TELEGRAM CONFIGURATION
# ═══════════════════════════════════════════════════════
TELEGRAM_BOT_TOKEN = "8954055830:AAGyE4TphKgrlR4OqHdhE64reXqdjC8Szsw"
LOG_GROUP_ID = "YOUR_GROUP_ID_HERE"
DEVELOPER_USERNAME = "@O_J_A_N_T_H_A"
SUPPORT_USERNAME   = "@O_J_A_N_T_H_A"

# ═══════════════════════════════════════════════════════
#  VOLTX API CONFIGURATION (UPDATED)
# ═══════════════════════════════════════════════════════
API_KEY          = "MIFEKXJYSUJ"
API_BASE         = "https://api.2oo9.cloud/MXS47FLFX0U/tnevs/@public/api"
API_URL          = f"{API_BASE}/getnum"
LIVE_ACCESS_URL  = f"{API_BASE}/liveaccess"
SUCCESS_OTP_URL  = f"{API_BASE}/success-otp"
CONSOLE_URL      = f"{API_BASE}/console"
DEFAULT_RID      = "26154"

# ═══════════════════════════════════════════════════════
#  GRAPHQL CHECKER CONSTANTS
# ═══════════════════════════════════════════════════════
GRAPHQL_CHECK_URL = "https://www.facebook.com/api/graphql/"
CHECK_LSD = "AdS-QY2mYrCcHP7sVf7ynTA6vTc"
CHECK_CIPHER_TEXT = (
    "AdAtB3O832KrYgWu2c7Jm2mNWOdAALA9wNFKJ_043RSsW27RSXXjhlBd0Cr8rGn-"
    "lIwgDuQU-CNQILiqKbqFW0GZop7nLgDVhClntKlePmNpHzT4ESf47v-lTUCNV3L-"
    "ikw70LhayHi30trSUJqk-Rvmaost-m0CTl60dFiIcbLNhGmQ8uggs-M1wfu04K"
    "QJvOQBDLwohSr7f_yRqkDGj98Ra-1S2N77k17Fqxu8N84cEWWTyv4qW6ySj7GI"
    "7CYYhD8QZDTzMxXcImxAr_Y"
)
CHECK_JAZOEST = "22291"
CHECK_DOC_ID = "27012969198380071"

# ═══════════════════════════════════════════════════════
#  PREMIUM UI COLORS
# ═══════════════════════════════════════════════════════
RED    = "\033[38;5;196m"
GREEN  = "\033[38;5;46m"
YELLOW = "\033[38;5;226m"
CYAN   = "\033[38;5;51m"
WHITE  = "\033[97m"
GRAY   = "\033[38;5;240m"
PINK   = "\033[38;5;205m"
BLUE   = "\033[38;5;39m"
BOLD   = "\033[1m"
RST    = "\033[0m"

LINE   = GRAY + "━"*60 + RST
EKL = GREEN + "➤" + RST

def clear_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{GREEN}{BOLD}
 ██████╗      ██╗ █████╗ ███╗   ██╗████████╗██╗  ██╗ █████╗ 
██╔═══██╗     ██║██╔══██╗████╗  ██║╚══██╔══╝██║  ██║██╔══██╗
██║   ██║     ██║███████║██╔██╗ ██║   ██║   ███████║███████║
██║   ██║██   ██║██╔══██║██║╚██╗██║   ██║   ██╔══██║██╔══██║
╚██████╔╝╚█████╔╝██║  ██║██║ ╚████║   ██║   ██║  ██║██║  ██║
 ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝

              ✦  @O_J_A_N_T_H_A  ✦


{GREEN}{BOLD}        FB REGISTRATION & GRAPHQL FILTER TOOL [v4.5 PRO]{RST}
{WHITE}{BOLD}        Developer : @O_J_A_N_T_H_A{RST}
{GREEN}        Version   : 4.5 ULTRA STRONG + BULLETPROOF REAL-TIME OTP{RST}

{GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RST}
""")

BROWSER_PROFILES = [
    {
        "profile": "chrome120",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "sec_ch_ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "platform": '"Windows"'
    },
    {
        "profile": "chrome124",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "sec_ch_ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "platform": '"Windows"'
    },
    {
        "profile": "chrome131",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec_ch_ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "platform": '"Windows"'
    },
    {
        "profile": "edge120",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "sec_ch_ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        "platform": '"Windows"'
    },
    {
        "profile": "firefox120",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "sec_ch_ua": None,
        "platform": None
    },
    {
        "profile": "firefox133",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "sec_ch_ua": None,
        "platform": None
    }
]

def parse_proxy(proxy_str):
    p = proxy_str.strip()
    if not p: return None
    if "://" not in p:
        parts = p.split(':')
        if len(parts) == 4:
            ip, port, user, pwd = parts
            url = f"http://{user}:{pwd}@{ip}:{port}"
        elif len(parts) == 2:
            url = f"http://{p}"
        else:
            return None
    else:
        url = p
    return {"http": url, "https": url}

def fetch_live_access():
    headers = {'mauthapi': API_KEY}
    for _ in range(3):
        try:
            resp = requests.get(LIVE_ACCESS_URL, headers=headers, timeout=10)
            if resp.status_code == 200:
                try: return resp.json()
                except: return resp.text
        except Exception:
            pass
        time.sleep(1)
    return None

def get_live_ranges_from_api():
    res = fetch_live_access()
    ranges = []
    
    items = []
    if isinstance(res, list):
        items = res
    elif isinstance(res, dict):
        items = res.get('data') or res.get('ranges') or res.get('result') or res.get('traffic') or []
        if not items:
            for k, v in res.items():
                if isinstance(v, dict):
                    v['id'] = v.get('id') or k
                    items.append(v)

    for item in items:
        if isinstance(item, dict):
            r_id = str(item.get('id') or item.get('range_id') or item.get('rid') or '')
            country = str(item.get('country') or item.get('name') or item.get('title') or item.get('service') or 'Live Range')
            code = str(item.get('code') or item.get('prefix') or item.get('dial_code') or '')
            traffic = str(item.get('traffic') or item.get('status') or item.get('speed') or 'High Access')
            if r_id:
                ranges.append({"id": r_id, "code": code, "country": country, "traffic": traffic})

    if not ranges:
        ranges = [
            {"id": "23762", "code": "+237", "country": "Cameroon 🇨🇲 (Live Traffic)", "traffic": "High Access"},
            {"id": "22505", "code": "+225", "country": "Cote d'Ivoire 🇨🇮 (Live Traffic)", "traffic": "High Access"},
            {"id": "22961", "code": "+229", "country": "Benin 🇧🇯 (Live Traffic)", "traffic": "Active"},
            {"id": "22896", "code": "+228", "country": "Togo 🇹🇬 (Live Traffic)", "traffic": "Active"},
            {"id": "23675", "code": "+236", "country": "Central African Republic 🇨🇫", "traffic": "Active"}
        ]
    return ranges

def live_traffic_ranges_monitor():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            clear_logo()
            print(f"{GREEN}{BOLD} ⚡ LIVE PANEL TRAFFIC & ACTIVE RANGES (REAL-TIME MONITOR) ⚡ {RST}\n")
            ranges = get_live_ranges_from_api()
            
            print(f" {WHITE}Last Update : {time.strftime('%Y-%m-%d %H:%M:%S')}{RST}")
            print(LINE)
            active_count = 0
            for idx, r in enumerate(ranges, 1):
                traffic_status = r['traffic'].lower()
                if any(k in traffic_status for k in ['high', 'active', 'fast', 'live', 'good', 'online']):
                    active_count += 1
                    status_color = GREEN
                else:
                    status_color = YELLOW
                
                print(f" {GREEN}[{idx}]{RST} {WHITE}RID: {r['id']} {GREEN}│{RST} {WHITE}{r['country']} ({r['code']}) {GREEN}│{RST} Traffic: {status_color}{r['traffic']}{RST}")
            
            print(LINE)
            print(f" {CYAN}Active Facebook/Live Traffic Ranges Found: {GREEN}{active_count}{RST}")
            print(f" {GRAY}(Auto-refreshing every 5 seconds... Press Ctrl+C to stop and go back){RST}")
            time.sleep(5)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[*] Exiting Live Traffic Monitor...{RST}\n")
        time.sleep(1)

def parse_number_response(resp):
    raw_text = resp.text.strip()
    c = clean_phone(raw_text)
    if c: return c
    try:
        j = resp.json()
        if isinstance(j, dict):
            data_val = j.get('data') or j.get('result') or j.get('number_info') or j.get('number')
            if isinstance(data_val, str):
                c = clean_phone(data_val)
                if c: return c
            elif isinstance(data_val, dict):
                for k in ['number', 'phone', 'num', 'mobile', 'msisdn']:
                    if k in data_val:
                        c = clean_phone(str(data_val[k]))
                        if c: return c
            for k in ['number', 'phone', 'num', 'mobile', 'msisdn', 'data']:
                if k in j and isinstance(j[k], (str, int)):
                    c = clean_phone(str(j[k]))
                    if c: return c
    except Exception:
        pass
    digits = re.findall(r'\+?\d{8,15}', raw_text)
    if digits:
        return digits[0]
    return None

def fetch_api_number(rid=DEFAULT_RID):
    headers = {
        'mauthapi': API_KEY,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    payload_keys = [
        {"rid": str(rid)},
        {"range_id": str(rid)},
        {"range": str(rid)},
        {"id": str(rid)}
    ]

    for _ in range(3):
        for p in payload_keys:
            try:
                resp = requests.post(API_URL, json=p, headers={**headers, 'Content-Type': 'application/json'}, timeout=8)
                if resp.status_code == 200 and resp.text.strip():
                    c = parse_number_response(resp)
                    if c: return c
            except Exception:
                pass

            try:
                resp = requests.post(API_URL, data=p, headers={**headers, 'Content-Type': 'application/x-www-form-urlencoded'}, timeout=8)
                if resp.status_code == 200 and resp.text.strip():
                    c = parse_number_response(resp)
                    if c: return c
            except Exception:
                pass

            try:
                resp = requests.get(f"{API_URL}?rid={rid}&range_id={rid}&range={rid}", headers=headers, timeout=8)
                if resp.status_code == 200 and resp.text.strip():
                    c = parse_number_response(resp)
                    if c: return c
            except Exception:
                pass
        time.sleep(0.2)

    return None

def fetch_console_feed(rid=DEFAULT_RID):
    headers = {'mauthapi': API_KEY, 'Content-Type': 'application/json'}
    endpoints = [
        CONSOLE_URL, 
        f"{API_BASE}/sms", 
        f"{API_BASE}/logs", 
        f"{API_BASE}/history",
        f"{API_BASE}/getotp",
        f"{API_BASE}/messages",
        f"{API_BASE}/active",
        f"{API_BASE}/check",
        f"{API_BASE}/status",
        f"{API_BASE}/otp",
        f"{API_BASE}/list",
        f"{API_BASE}/getnums",
        f"{API_BASE}/all",
        f"{API_BASE}/feed"
    ]
    all_results = []
    for endpoint_url in endpoints:
        for suffix in [f"?rid={rid}", f"?range_id={rid}", f"?limit=500", f""]:
            target = endpoint_url + suffix if "?" in endpoint_url or not suffix else endpoint_url + suffix
            try:
                resp = requests.get(target, headers=headers, timeout=3)
                if resp.status_code == 200 and resp.text.strip():
                    try: 
                        j_res = resp.json()
                        if j_res: all_results.append(j_res)
                    except: 
                        all_results.append(resp.text)
            except Exception:
                pass
            
            try:
                resp = requests.post(endpoint_url, json={"rid": str(rid), "limit": 500}, headers=headers, timeout=3)
                if resp.status_code == 200 and resp.text.strip():
                    try: 
                        j_res = resp.json()
                        if j_res: all_results.append(j_res)
                    except: 
                        all_results.append(resp.text)
            except Exception:
                pass
    return all_results if all_results else None

def report_success_otp(number, uid=""):
    headers = {'mauthapi': API_KEY, 'Content-Type': 'application/json'}
    payload = {"number": number, "uid": uid}
    for _ in range(2):
        try:
            resp = requests.post(SUCCESS_OTP_URL, json=payload, headers=headers, timeout=8)
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        time.sleep(0.2)
    return None

def check_number_graphql(phone_number):
    for _ in range(3):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.facebook.com',
                'referer': 'https://www.facebook.com/login/identify/',
                'x-fb-lsd': CHECK_LSD, 'x-asbd-id': '359341',
                'x-fb-friendly-name': 'CAAFBAccountSearchViewQuery',
                'accept-language': 'en-US,en;q=0.9',
            }
            variables = {'params': {
                'cipher_text': CHECK_CIPHER_TEXT, 'context': 'recover',
                'event_request_id': str(uuid.uuid4()),
                'friend_name': '', 'search_query': phone_number,
                'waterfall_id': str(uuid.uuid4()),
            }}
            payload = {
                '__a': '1', '__req': '5', 'lsd': CHECK_LSD, 'jazoest': CHECK_JAZOEST,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CAAFBAccountSearchViewQuery',
                'variables': json.dumps(variables, separators=(',',':')),
                'doc_id': CHECK_DOC_ID,
            }
            r = requests.post(GRAPHQL_CHECK_URL, headers=headers, data=payload, timeout=12, impersonate="chrome124")
            if r.status_code == 200:
                text_resp = r.text
                if text_resp.startswith("for (;;);"): text_resp = text_resp[9:]
                js = json.loads(text_resp)
                data = js.get('data') or {}
                search = data.get('caa_ar_fb_account_search') or {}
                accounts = search.get('accounts') or []
                err = (search.get('error_content') or {}).get('description') or ''

                if not accounts and ('No account found' in err or not accounts): 
                    return 'free'
                if accounts: 
                    return 'taken'
        except Exception:
            pass
        time.sleep(0.3)
    return 'free'

_LSD_RE = [
    re.compile(r'"LSD",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),
    re.compile(r'"lsd":\s*"([^"]+)"'), 
    re.compile(r'name="lsd"\s+value="([^"]+)"'),
    re.compile(r'\["LSD",\[\],\{"token":"([^"]+)"\}')
]
_REV_RE = [re.compile(r'"server_revision":\s*(\d+)'), re.compile(r'"__rev":\s*(\d+)')]
_HSI_RE = [re.compile(r'"hsi":\s*"(\d+)"'), re.compile(r'"__hsi":\s*"(\d+)"')]
_SPINB  = [re.compile(r'"__spin_b":\s*"([^"]+)"')]
_SPINT  = [re.compile(r'"__spin_t":\s*(\d+)')]
_HS_RE  = [re.compile(r'"__hs":\s*"([^"]+)"'), re.compile(r'"haste_session":\s*"([^"]+)"')]
_COMET  = [re.compile(r'"comet_env":\s*(\d+)')]
_DTSG   = [
    re.compile(r'"DTSGInitData",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),
    re.compile(r'"DTSGInitialData",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),
    re.compile(r'name="fb_dtsg"\s+value="([^"]+)"'), 
    re.compile(r'"fb_dtsg":\s*"([^"]+)"')
]
_HSDP   = re.compile(r'"__hsdp"\s*:\s*"([^"]*)"')
_HBLP   = re.compile(r'"__hblp"\s*:\s*"([^"]*)"')
_SJSP   = re.compile(r'"__sjsp"\s*:\s*"([^"]*)"')
_PUBKEY = re.compile(r'"key_id"\s*:\s*(\d+)[^}]{0,80}"public_key"\s*:\s*"([0-9a-fA-F]{40,})"')
_PUBKEY2= re.compile(r'"public_key"\s*:\s*"([0-9a-fA-F]{40,})"[^}]{0,80}"key_id"\s*:\s*(\d+)')
_CSR    = re.compile(r'"__csr"\s*:\s*"([^"]*)"')

def extract_tokens(html, session_cookies=None, **d):
    t = {}
    t['lsd']       = next((m.group(1) for p in _LSD_RE for m in [p.search(html)] if m), d.get('default_lsd','AVq13289v2'))
    t['rev']       = next((m.group(1) for p in _REV_RE for m in [p.search(html)] if m), d.get('default_rev','1012548900'))
    t['hsi']       = next((m.group(1) for p in _HSI_RE for m in [p.search(html)] if m), d.get('default_hsi','73428910492819'))
    t['spin_b']    = next((m.group(1) for p in _SPINB for m in [p.search(html)] if m), d.get('default_spin_b','trunk'))
    t['spin_t']    = next((m.group(1) for p in _SPINT for m in [p.search(html)] if m), d.get('default_spin_t', str(int(time.time()))))
    t['hs']        = next((m.group(1) for p in _HS_RE for m in [p.search(html)] if m), d.get('default_hs','23589.client_page.0.0.0'))
    t['comet_req'] = next((m.group(1) for p in _COMET for m in [p.search(html)] if m), d.get('default_comet_req','102'))
    t['fb_dtsg']   = next((m.group(1) for p in _DTSG for m in [p.search(html)] if m), '')
    t['csr']       = (m := _CSR.search(html)) and m.group(1) or ''
    _dyn_m = re.search(r'"__dyn":"([^"]+)"', html)
    t['dyn']       = _dyn_m.group(1) if _dyn_m else d.get('default_dyn', REG_DYN)
    
    if session_cookies:
        try:
            all_v = ''.join(session_cookies.get_dict().values())
            t['jazoest'] = '2' + str(sum(ord(c) for c in all_v))
        except:
            t['jazoest'] = d.get('default_jazoest', '22431')
    else:
        t['jazoest'] = d.get('default_jazoest', '22431')
    return t

def extract_dyn(html):
    hsdp = (_HSDP.findall(html) or [''])[0]
    hblp = (_HBLP.findall(html) or [''])[0]
    sjsp = (_SJSP.findall(html) or [''])[0]
    return {'hsdp': hsdp, 'hblp': hblp, 'sjsp': sjsp}

def extract_pubkey(html):
    m = _PUBKEY.search(html)
    if m: return int(m.group(1)), m.group(2)
    m = _PUBKEY2.search(html)
    if m: return int(m.group(2)), m.group(1)
    for block in re.findall(r'<script[^>]*>(.*?)</script>', html, re.S):
        m = _PUBKEY.search(block)
        if m: return int(m.group(1)), m.group(2)
        m = _PUBKEY2.search(block)
        if m: return int(m.group(2)), m.group(1)
    return None, None

_CLEAN = re.compile(r'[\s\-\(\)\.]')
_PHONE = re.compile(r'^\+?\d{7,15}$')

def clean_phone(v):
    if not v: return None
    c = _CLEAN.sub('', str(v).strip())
    return c if _PHONE.match(c) else None

def read_phones(filepath):
    if not os.path.exists(filepath): return []
    lines = []
    for enc in ['utf-8','utf-8-sig','cp1252','latin-1']:
        try:
            with open(filepath,'r',encoding=enc) as f: lines = f.readlines()
            break
        except: continue
    nums = []
    for line in lines:
        c = clean_phone(line.strip())
        if c: nums.append(c)
    return nums

print_lock   = threading.Lock()
counter_lock = threading.Lock()
file_lock    = threading.Lock()

total_checked = 0
total_success = 0
total_failed  = 0
total_error   = 0

SUCCESSFUL_ACCOUNTS_LOG = []

def reset_counters():
    global total_checked, total_success, total_failed, total_error, SUCCESSFUL_ACCOUNTS_LOG
    total_checked = total_success = total_failed = total_error = 0
    SUCCESSFUL_ACCOUNTS_LOG = []

def _bar():
    return (f"\r{GREEN}[YS-SECURE]{RST} CHECKED:{total_checked}"
            f" {GREEN}|{RST} {GREEN}SUCCESS:{total_success}"
            f" {GREEN}|{RST} {GREEN}FAILED:{total_failed}"
            f" {GREEN}|{RST} {RED}ERROR:{total_error}{RST}")

def safe_print(text):
    with print_lock:
        sys.stdout.write('\r' + ' '*80 + '\r')
        try: sys.stdout.write(str(text) + '\n')
        except UnicodeEncodeError:
            sys.stdout.write(str(text).encode('utf-8', errors='ignore').decode() + '\n')
        sys.stdout.write(_bar())
        sys.stdout.flush()

def update_counter(status, number=None, message=None, color=None):
    global total_checked, total_success, total_failed, total_error
    with counter_lock:
        if   status == "success": total_success += 1
        elif status == "failed":  total_failed  += 1
        elif status == "error":   total_error   += 1
        total_checked += 1
    if message:
        safe_print(f"{color or WHITE} {message} {number or ''}{RST}")
    else:
        with print_lock:
            sys.stdout.write(_bar())
            sys.stdout.flush()

def save_line(filename, text):
    with file_lock:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(str(text) + '\n')

FIRST_NAMES = [
    "James","John","Robert","Michael","William","David","Richard","Joseph",
    "Thomas","Charles","Christopher","Daniel","Matthew","Anthony","Mark",
    "Mary","Patricia","Jennifer","Linda","Elizabeth","Barbara","Susan"
]

LAST_NAMES = [
    "Smith","Johnson","Williams","Brown","Jones","Miller","Davis","Garcia",
    "Rodriguez","Wilson","Martinez","Anderson","Taylor","Thomas","Hernandez"
]

USER_PASSWORD = "Okabye#570"

REG_DYN = ("7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W099w8G1Dz81s8hw"
           "GwQw9m1YwBgao6C0Mo2swaOfK0EUjwGzE2ZwNwmE2eUlwhE2Lw6OyES1Tw8W0Lo6-1"
           "Fw4mwr86C1nwqU8XwnqwIwtU26wbu1ww3dU")

def rand_name():
    return random.choice(FIRST_NAMES), random.choice(LAST_NAMES)

def rand_dob():
    yr = time.localtime().tm_year
    return random.randint(1975, yr-18), random.randint(1,12), random.randint(1,28)

def gen_s():
    c = string.ascii_lowercase + string.digits
    return ':'.join(''.join(random.choices(c, k=6)) for _ in range(3))

def strip_json(text):
    return text[9:] if text.startswith("for (;;);") else text

def encrypt_password_simple(password):
    return f"#PWD_BROWSER:0:{int(time.time())}:{password}"

def encrypt_password_v5(password, pub_key_hex, pub_key_id):
    try:
        from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        from cryptography.hazmat.backends import default_backend
        import base64, os as _os

        timestamp = int(time.time())
        pub_key_bytes = bytes.fromhex(pub_key_hex)
        pub_key = serialization.load_der_public_key(pub_key_bytes, backend=default_backend())

        aes_key = _os.urandom(32)
        iv = _os.urandom(12)

        aad = str(timestamp).encode('utf-8')
        aesgcm = AESGCM(aes_key)
        ct_with_tag = aesgcm.encrypt(iv, password.encode('utf-8'), aad)
        ciphertext = ct_with_tag[:-16]
        tag = ct_with_tag[-16:]

        enc_aes_key = pub_key.encrypt(aes_key, asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(), label=None
        ))

        payload = bytes([5, pub_key_id & 0xFF]) + iv + enc_aes_key + tag + ciphertext
        b64 = base64.b64encode(payload).decode('ascii')
        return f"#PWD_BROWSER:5:{timestamp}:{b64}"
    except Exception:
        return encrypt_password_simple(password)

def build_common(tokens, s_val, dyn, req_num='1'):
    return {
        'av': '0', '__user': '0', '__a': '1', '__req': req_num,
        '__hs': tokens['hs'], 'dpr': '1', '__ccg': 'EXCELLENT',
        '__rev': tokens['rev'], '__s': s_val,
        '__hsi': tokens['hsi'], '__dyn': tokens.get('dyn', REG_DYN),
        '__csr': tokens.get('csr', ''),
        '__hsdp': dyn['hsdp'], '__hblp': dyn['hblp'], '__sjsp': dyn['sjsp'],
        '__comet_req': tokens.get('comet_req', '102'),
        'lsd': tokens['lsd'], 'jazoest': tokens['jazoest'],
        '__spin_r': tokens['rev'], '__spin_b': tokens['spin_b'],
        '__spin_t': tokens['spin_t'], '__jssesw': '1',
    }

def process_number(number, password=USER_PASSWORD, proxy=None, bot_instance=None, chat_id=None, user_info=None, rid=DEFAULT_RID):
    formatted_num = f"+{number}" if not str(number).startswith("+") else str(number)
    clean_num = formatted_num.lstrip("+")
    
    safe_print(f"{CYAN}[GRAPHQL CHECK] Filtering fresh number {WHITE}{formatted_num}{CYAN}...{RST}")
    check_status = check_number_graphql(formatted_num)
    
    if check_status == 'taken':
        update_counter("failed", number, f"Already Taken (Has FB Account) - Skipping", YELLOW)
        save_line('Taken_Numbers.txt', clean_num)
        return
    
    safe_print(f"{GREEN}[FREE] Number is fresh and ready! Starting fast registration...{RST}")
    save_line('Free_Numbers.txt', clean_num)

    for reg_attempt in range(1, len(BROWSER_PROFILES) + 1):
        browser_cfg = BROWSER_PROFILES[reg_attempt - 1]
        impersonate_profile = browser_cfg["profile"]
        user_agent = browser_cfg["ua"]
        sec_ch_ua = browser_cfg["sec_ch_ua"]
        platform = browser_cfg["platform"]

        try:
            session = requests.Session()
            if proxy: session.proxies.update(proxy)

            try:
                session.get("https://www.facebook.com/", headers={'user-agent': user_agent}, impersonate=impersonate_profile, timeout=10)
            except:
                pass

            page_h = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none', 'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1', 'user-agent': user_agent,
                'cache-control': 'max-age=0'
            }
            if sec_ch_ua:
                page_h['sec-ch-ua'] = sec_ch_ua
                page_h['sec-ch-ua-mobile'] = '?0'
                page_h['sec-ch-ua-platform'] = platform

            reg_url = ('https://www.facebook.com/reg/?entry_point=login'
                       '&next=https%3A%2F%2Fwww.facebook.com%2Fconfirmemail.php'
                       '%3Fnext%3Dhttps%253A%252F%252Fwww.facebook.com%252F')

            resp = None
            try:
                resp = session.get(reg_url, headers=page_h, impersonate=impersonate_profile, timeout=12)
            except Exception:
                pass

            if not resp or resp.status_code != 200 or len(resp.text) < 500:
                continue

            html   = resp.text
            tokens = extract_tokens(html, session_cookies=session.cookies, default_comet_req="102")
            dyn    = extract_dyn(html)
            pub_key_id, pub_key_hex = extract_pubkey(html)

            lsd = tokens['lsd']
            api_h = {
                'accept': '*/*', 'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.facebook.com', 'referer': resp.url,
                'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin', 'x-asbd-id': '359341',
                'x-fb-friendly-name': 'useCAARegistrationFormSubmitMutation',
                'x-fb-lsd': lsd, 'user-agent': user_agent
            }
            if sec_ch_ua:
                api_h['sec-ch-ua'] = sec_ch_ua
                api_h['sec-ch-ua-mobile'] = '?0'
                api_h['sec-ch-ua-platform'] = platform

            if pub_key_id and pub_key_hex:
                fmt_pwd = encrypt_password_v5(password, pub_key_hex, pub_key_id)
            else:
                fmt_pwd = encrypt_password_simple(password)

            first, last = rand_name()
            yr, mo, dy  = rand_dob()
            waterfall_id = str(uuid.uuid4())
            mutation_id  = str(uuid.uuid4())

            variables = json.dumps({
                "input": {
                    "actor_id": "0", "client_mutation_id": mutation_id, "machine_id": "",
                    "reg_data": {
                        "birthday_day": dy, "birthday_month": mo, "birthday_year": yr,
                        "contactpoint": {"sensitive_string_value": clean_num},
                        "contactpoint_type": "PHONE", "custom_gender": "",
                        "did_use_age": False, "firstname": {"sensitive_string_value": first},
                        "fullname": {"sensitive_string_value": f"{first} {last}"},
                        "ig_age_block_data": None, "lastname": {"sensitive_string_value": last},
                        "preferred_pronoun": None, "reg_passwd__": {"sensitive_string_value": fmt_pwd},
                        "sex": "MALE", "use_custom_gender": False, "username": {"sensitive_string_value": ""},
                    },
                    "sk_pipa_consent_given": None, "waterfall_id": waterfall_id,
                }
            }, separators=(',', ':'))

            post_data = {
                **build_common(tokens, gen_s(), dyn, req_num='u'),
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useCAARegistrationFormSubmitMutation',
                'server_timestamps': 'true', 'variables': variables,
                'doc_id': '25782408224726258', 'qpl_active_flow_ids': '250359044,516759801',
                'fb_api_analytics_tags': '["qpl_active_flow_ids=250359044,516759801"]',
                'fb_dtsg': tokens.get('fb_dtsg', ''),
            }

            resp2 = None
            try:
                resp2 = session.post('https://www.facebook.com/api/graphql/', headers=api_h, data=post_data, impersonate=impersonate_profile, timeout=15)
            except Exception:
                pass

            if not resp2 or resp2.status_code != 200:
                continue

            try:
                j = json.loads(strip_json(resp2.text))
            except json.JSONDecodeError:
                continue

            errors = j.get("errors", [])
            if errors:
                ec = errors[0].get("api_error_code", errors[0].get("code", "?"))
                update_counter("failed", number, f"API Error {ec}", RED)
                save_line('Failed_Numbers.txt', clean_num)
                return

            data = j.get("data", {})
            reg_result = (data.get("caa_registration_homepage_submit") or
                          data.get("caa_registration_form_submit") or
                          data.get("registration_form_submit") or {})

            status = reg_result.get("status", "")
            merged_cookies = session.cookies.get_dict()
            merged_cookies.update(resp2.cookies.get_dict())
            c_user = merged_cookies.get("c_user", "") or reg_result.get("account_id") or reg_result.get("user_id") or ""

            is_success = False
            if c_user and len(str(c_user)) > 5 or status in ("SUCCESS", "OTP_SENT", "CONFIRM_EMAIL"):
                is_success = True

            if is_success:
                cookie_str = "; ".join([f"{k}={v}" for k, v in merged_cookies.items()])

                safe_print(f"{GREEN}{BOLD} ✔ ACCOUNT CREATED SUCCESSFULLY{RST}")
                safe_print(f"{GREEN} ├─ Number   : {WHITE}{clean_num}")
                safe_print(f"{GREEN} ├─ Name     : {WHITE}{first} {last}")
                safe_print(f"{GREEN} ├─ Password : {GREEN}{password}")
                safe_print(f"{GREEN} ├─ Account  : {WHITE}{c_user}")
                safe_print(f"{GREEN} ├─ RID      : {WHITE}{rid}")

                update_counter("success", clean_num, None)
                save_line('Success_Numbers.txt', f"{clean_num}|{c_user}|{password}|{cookie_str}")
                
                report_success_otp(clean_num, str(c_user))

                with counter_lock:
                    SUCCESSFUL_ACCOUNTS_LOG.append({
                        "number": f"+{clean_num}",
                        "uid": c_user,
                        "otp": "PENDING",
                        "bot": bot_instance,
                        "chat_id": chat_id,
                        "rid": rid
                    })

                if chat_id and user_info:
                    increment_user_success(chat_id, user_info, 1)

                if bot_instance and chat_id:
                    msg_text = (
                        f"✅ *FB Account Created Successfully!*\n\n"
                        f"👤 *Name:* `{first} {last}`\n"
                        f"📞 *Number:* `{clean_num}`\n"
                        f"🔑 *Password:* `{password}`\n"
                        f"🆔 *UID:* `{c_user}`\n"
                        f"📌 *RID:* `{rid}`\n"
                        f"👤 *User:* `{user_info}`\n"
                        f"👑 *Tool Developed By:* `@O_J_A_N_T_H_A`"
                    )
                    try:
                        bot_instance.send_message(chat_id, msg_text, parse_mode='Markdown')
                    except:
                        pass
                return
            else:
                continue

        except Exception:
            continue

    update_counter("failed", clean_num, f"Failed/Blocked", RED)
    save_line('Failed_Numbers.txt', clean_num)

# Real-time Dual Box Terminal Display (Clean Refresh)
def print_dual_boxes():
    with counter_lock:
        success_list = [acc for acc in SUCCESSFUL_ACCOUNTS_LOG]
        waiting_list = [acc for acc in SUCCESSFUL_ACCOUNTS_LOG if acc["otp"] in ["PENDING", "------", "TIMEOUT"]]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{GREEN}{BOLD} ⚡ VOLTX PANEL LIVE OTP DASHBOARD (AUTO-POLLING 1s) ⚡ {RST}\n")

    # Box 1: Success Accounts Created Box
    print(f"{GREEN}┌" + "─"*56 + f"┐{RST}")
    print(f"{GREEN}│ {BOLD}SUCCESS ACCOUNTS BOX ({len(success_list)})".ljust(57) + f"{GREEN}│{RST}")
    print(f"{GREEN}├" + "─"*56 + f"┤{RST}")
    if success_list:
        for acc in success_list[-6:]:  # Last 6 records
            otp_disp = acc['otp'] if acc['otp'] not in ["PENDING", "TIMEOUT", "------"] else f"{YELLOW}PENDING (Waiting OTP){RST}"
            line_str = f" 📞 {acc['number']} ➔ OTP: {otp_disp}"
            print(f"{GREEN}│{RST} {WHITE}{line_str}".ljust(57) + f"{GREEN}│{RST}")
    else:
        print(f"{GREEN}│{RST} {GRAY} No successful accounts yet...".ljust(57) + f"{GREEN}│{RST}")
    print(f"{GREEN}└" + "─"*56 + f"┘{RST}")

    # Box 2: Waiting For OTP Box
    print(f"{YELLOW}┌" + "─"*56 + f"┐{RST}")
    print(f"{YELLOW}│ {BOLD}WAITING FOR OTP BOX (ACTIVE POLLING 1s)".ljust(57) + f"{YELLOW}│{RST}")
    print(f"{YELLOW}├" + "─"*56 + f"┤{RST}")
    if waiting_list:
        for acc in waiting_list:
            line_str = f" ⏳ Waiting OTP for: {WHITE}{acc['number']}{YELLOW} [RID: {acc.get('rid','26154')}]"
            print(f"{YELLOW}│{RST} {WHITE}{line_str}".ljust(57) + f"{YELLOW}│{RST}")
    else:
        print(f"{YELLOW}│{RST} {GREEN} All OTPs received successfully!".ljust(57) + f"{YELLOW}│{RST}")
    print(f"{YELLOW}└" + "─"*56 + f"┘{RST}\n")

def extract_otp_from_json(data, full_num, last_digits):
    if not data:
        return None
    
    if isinstance(data, list):
        for item in data:
            res = extract_otp_from_json(item, full_num, last_digits)
            if res: return res
        return None

    if isinstance(data, str):
        try:
            data = json.loads(data)
        except:
            clean_full = full_num.lstrip("+")
            clean_last = last_digits.lstrip("+")
            if clean_full in data or clean_last in data or clean_last[-6:] in data:
                codes = re.findall(r'\b\d{4,6}\b', data)
                for c in codes:
                    if c != clean_full and c != clean_last and len(c) in [4, 5, 6] and not c.startswith("237"):
                        return c
            return None

    items = []
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        items.append(data)
        for k in ['data', 'result', 'messages', 'sms', 'logs', 'history', 'items', 'list', 'traffic', 'numbers', 'content', 'records', 'sms_list', 'smslist']:
            if k in data and isinstance(data[k], (list, dict)):
                if isinstance(data[k], list): items.extend(data[k])
                else: items.append(data[k])

    clean_full = full_num.lstrip("+")
    clean_last = last_digits.lstrip("+")

    for item in items:
        if isinstance(item, dict):
            item_str = json.dumps(item)
            item_num = str(item.get('number') or item.get('phone') or item.get('msisdn') or item.get('to') or '')
            clean_item_num = item_num.lstrip("+")
            msg_text = str(item.get('sms') or item.get('message') or item.get('text') or item.get('content') or item.get('otp') or item_str)
            
            # Match number without '+' sign perfectly
            if clean_full in clean_item_num or clean_last in clean_item_num or clean_last[-6:] in clean_item_num or clean_full in item_str or clean_last in item_str:
                codes = re.findall(r'\b\d{4,6}\b', msg_text)
                for c in codes:
                    if c != clean_full and c != clean_last and len(c) in [4, 5, 6] and not c.startswith("237") and c != clean_last[-6:]:
                        return c
        elif isinstance(item, str):
            if clean_full in item or clean_last in item or clean_last[-6:] in item:
                codes = re.findall(r'\b\d{4,6}\b', item)
                for c in codes:
                    if c != clean_full and c != clean_last and len(c) in [4, 5, 6] and not c.startswith("237"):
                        return c

    full_dump = json.dumps(data)
    if clean_full in full_dump or clean_last in full_dump or clean_last[-6:] in full_dump:
        matches = re.findall(r'(\d{4,6})', full_dump)
        for m in matches:
            if m != clean_full and m != clean_last and len(m) in [4, 5, 6] and not m.startswith("237") and m != clean_last[-6:]:
                return m

    return None

def realtime_otp_worker(stop_event):
    while not stop_event.is_set():
        try:
            with counter_lock:
                pending_accs = [acc for acc in SUCCESSFUL_ACCOUNTS_LOG if acc["otp"] in ["PENDING", "------", "TIMEOUT"]]
            
            if pending_accs:
                headers = {'mauthapi': API_KEY, 'Content-Type': 'application/json'}
                
                for acc in pending_accs:
                    if stop_event.is_set():
                        break
                    full_num = acc["number"].lstrip("+")
                    last_digits = full_num[-8:] if len(full_num) >= 8 else full_num
                    acc_rid = acc.get("rid", DEFAULT_RID)
                    
                    found_otp = None
                    
                    # 1. Query specific endpoints with both with and without '+' variants
                    number_endpoints = [
                        f"{API_BASE}/sms?number={full_num}&rid={acc_rid}",
                        f"{API_BASE}/getotp?number={full_num}&rid={acc_rid}",
                        f"{API_BASE}/console?number={full_num}&rid={acc_rid}",
                        f"{API_BASE}/sms?number=+{full_num}&rid={acc_rid}",
                        f"{API_BASE}/sms?number={full_num}",
                        f"{API_BASE}/getotp?number={full_num}",
                        f"{API_BASE}/console?rid={acc_rid}",
                        f"{API_BASE}/messages?number={full_num}&rid={acc_rid}"
                    ]
                    for ep in number_endpoints:
                        try:
                            r = requests.get(ep, headers=headers, timeout=2)
                            if r.status_code == 200 and r.text.strip():
                                res_data = r.json() if r.headers.get('content-type', '').startswith('application/json') else r.text
                                found_otp = extract_otp_from_json(res_data, full_num, last_digits)
                                if found_otp: break
                        except:
                            pass

                        try:
                            r = requests.post(ep, json={"number": full_num, "rid": str(acc_rid)}, headers=headers, timeout=2)
                            if r.status_code == 200 and r.text.strip():
                                res_data = r.json() if r.headers.get('content-type', '').startswith('application/json') else r.text
                                found_otp = extract_otp_from_json(res_data, full_num, last_digits)
                                if found_otp: break
                        except:
                            pass

                    # 2. Fallback to global console feed
                    if not found_otp:
                        console_data = fetch_console_feed(rid=acc_rid)
                        if console_data:
                            found_otp = extract_otp_from_json(console_data, full_num, last_digits)
                    
                    if found_otp:
                        with counter_lock:
                            acc["otp"] = found_otp
                        
                        safe_print(f"\n{GREEN}{BOLD} ⚡ [REAL OTP RECEIVED INSTANTLY] Number: {WHITE}{acc['number']} {GREEN}➔ OTP: {YELLOW}{BOLD}{found_otp}{RST}\n"
                                   f"{GREEN} └─ Format : {WHITE}<#> {found_otp} is your Facebook code H2{RST}\n")
                        
                        if acc.get("bot") and acc.get("chat_id"):
                            try:
                                acc["bot"].send_message(
                                    acc["chat_id"],
                                    f"🔔 *Real OTP Received!*\n\n📞 *Number:* `{acc['number']}`\n🔑 *OTP:* `{found_otp}`\n💬 *Format:* `<#> {found_otp} is your Facebook code H2`",
                                    parse_mode='Markdown'
                                )
                            except:
                                pass
                
                print_dual_boxes()
        except Exception:
            pass
        time.sleep(1)

user_sessions = {}
ALL_USERS_FILE = "bot_users.json"
USER_STATS_FILE = "user_stats.json"

def load_all_users():
    if os.path.exists(ALL_USERS_FILE):
        try:
            with open(ALL_USERS_FILE, 'r') as f: return set(json.load(f))
        except: return set()
    return set()

def save_user_id(chat_id):
    users = load_all_users()
    if chat_id not in users:
        users.add(chat_id)
        try:
            with open(ALL_USERS_FILE, 'w') as f: json.dump(list(users), f)
        except: pass

def load_user_stats():
    if os.path.exists(USER_STATS_FILE):
        try:
            with open(USER_STATS_FILE, 'r') as f: return json.load(f)
        except: return {}
    return {}

def increment_user_success(chat_id, user_name, count=1):
    stats = load_user_stats()
    str_id = str(chat_id)
    if str_id not in stats:
        stats[str_id] = {"name": user_name, "success_count": 0}
    stats[str_id]["name"] = user_name
    stats[str_id]["success_count"] += count
    try:
        with open(USER_STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=4)
    except: pass

def display_final_summary():
    start_wait = time.time()
    max_wait_time = 1800
    
    while time.time() - start_wait < max_wait_time:
        with counter_lock:
            pending = [a for a in SUCCESSFUL_ACCOUNTS_LOG if a["otp"] in ["PENDING", "------", "TIMEOUT"]]
        if not pending:
            break
        time.sleep(1)

    with counter_lock:
        for acc in SUCCESSFUL_ACCOUNTS_LOG:
            if acc["otp"] in ["PENDING", "------"]:
                acc["otp"] = "TIMEOUT"
    
    print(f"\n{CYAN}┌" + "─"*56 + "┐{RST}")
    print(f"{CYAN}│ {BOLD}OTP HISTORY ({len(SUCCESSFUL_ACCOUNTS_LOG)})".ljust(57) + f"{CYAN}│{RST}")
    print(f"{CYAN}├" + "─"*56 + "┤{RST}")
    for idx, acc in enumerate(SUCCESSFUL_ACCOUNTS_LOG, 1):
        otp_val = acc['otp'] if acc['otp'] not in ["PENDING", "TIMEOUT", "------"] else "------"
        line_str = f" [{idx}] {acc['number']} - Facebook - <#> {otp_val} is your Facebook code H2"
        print(f"{GREEN}│{RST} {WHITE}{line_str}".ljust(57) + f"{CYAN}│{RST}")
    print(f"{CYAN}├" + "─"*56 + "┤{RST}")
    print(f"{CYAN}│ {BOLD}✦ SUCCESSFULLY CREATED NUMBERS ✦".ljust(57) + f"{CYAN}│{RST}")
    print(f"{CYAN}├" + "─"*56 + "┤{RST}")
    num_list_str = "   ".join([acc['number'] for acc in SUCCESSFUL_ACCOUNTS_LOG])
    print(f"{GREEN}│{RST} {WHITE}{num_list_str}".ljust(57) + f"{GREEN}│{RST}")
    print(f"{CYAN}└" + "─"*56 + "┘{RST}\n")
    print(f"{GREEN}⌛ Done! All processes completed successfully.{RST}")
    print(f"{RED}🔴 Press Ctrl+C to exit{RST}\n")

def start_telegram_bot():
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print(f"{RED}[!] Please configure TELEGRAM_BOT_TOKEN in the script first!{RST}")
        return

    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

    def main_menu_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("➕ Create Account")
        btn2 = types.KeyboardButton("📊 Live Range / Traffic")
        btn3 = types.KeyboardButton("🌐 Global Live Feed")
        btn4 = types.KeyboardButton("👤 SUPPORT")
        markup.add(btn1, btn2, btn3, btn4)
        return markup

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        save_user_id(message.chat.id)
        bot.send_message(
            message.chat.id, 
            "স্বাগতম! ফেইসবুক অ্যাকাউন্ট রেজিস্ট্রেশন ও গ্রাফকিউল ফিল্টার টুলে (v4.5 PRO)\n\nDeveloper: @O_J_A_N_T_H_A", 
            reply_markup=main_menu_keyboard()
        )

    @bot.message_handler(func=lambda m: True)
    def handle_messages(message):
        chat_id = message.chat.id
        text = message.text.strip()
        save_user_id(chat_id)

        if text == "➕ Create Account":
            fetched_ranges = get_live_ranges_from_api()
            user_sessions[chat_id] = {'step': 'selecting_range', 'ranges': fetched_ranges}
            
            markup = types.InlineKeyboardMarkup(row_width=1)
            for idx, r in enumerate(fetched_ranges):
                btn_text = f"{r['country']} ({r['code']}) - [{r['traffic']}]"
                markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"rid_{idx}"))
            
            bot.send_message(
                chat_id, 
                "🌐 *প্যানেল থেকে রিয়েল-টাইম লাইভ ট্রাফিক রেইঞ্জগুলো ফেচ করা হয়েছে:*\n\nনিচের লিস্ট থেকে যে রেইঞ্জে আইডি খুলতে চান সেটি সিলেক্ট করুন:", 
                parse_mode='Markdown', 
                reply_markup=markup
            )
            return

        elif text == "📊 Live Range / Traffic":
            data = fetch_live_access()
            text_data = json.dumps(data, indent=2) if data else "No data available"
            if len(text_data) > 4000: text_data = text_data[:3996] + "\n..."
            bot.reply_to(message, f"📊 *Live Access / Traffic Ranges:*\n```json\n{text_data}\n```", parse_mode='Markdown', reply_markup=main_menu_keyboard())
            return
        elif text == "🌐 Global Live Feed":
            data = fetch_console_feed()
            text_data = json.dumps(data, indent=2) if data else "No data available"
            if len(text_data) > 4000: text_data = text_data[:3996] + "\n..."
            bot.reply_to(message, f"🌐 *Global Live Console Feed:*\n```json\n{text_data}\n```", parse_mode='Markdown', reply_markup=main_menu_keyboard())
            return
        elif text == "👤 SUPPORT":
            bot.reply_to(message, f"🛠 যে কোনো প্রয়োজনে যোগাযোগ করুন:\nDeveloper: @O_J_A_N_T_H_A", reply_markup=main_menu_keyboard())
            return

        if chat_id not in user_sessions:
            user_sessions[chat_id] = {'step': 'waiting_count'}

        state = user_sessions[chat_id]
        
        if state.get('step') == 'waiting_count':
            try:
                count = int(text)
                if count <= 0: raise ValueError()
            except:
                bot.reply_to(message, "❌ অনুগ্রহ করে সঠিক সংখ্যা দিন (যেমন: 5)", reply_markup=main_menu_keyboard())
                return
            state['count'] = count
            state['step'] = 'waiting_password'
            bot.reply_to(message, f"✅ মোট {count}টি অ্যাকাউন্ট তৈরির জন্য সিলেকশন সম্পন্ন হয়েছে। এখন পাসওয়ার্ড (Password) দিন:", reply_markup=main_menu_keyboard())
        
        elif state.get('step') == 'waiting_password':
            password = text
            count = state.get('count', 1)
            selected_rid = state.get('rid', DEFAULT_RID)
            user = message.from_user
            user_info = f"{user.first_name} (@{user.username})" if user.username else str(user.id)

            bot.reply_to(message, f"🚀 রেইঞ্জ ID: `{selected_rid}` থেকে নাম্বার নিয়ে Fast Batch Creation শুরু হয়েছে! মোট {count}টি সফল অ্যাকাউন্ট টার্গেট।", parse_mode='Markdown', reply_markup=main_menu_keyboard())
            
            def run_bot_process():
                reset_counters()
                stop_event = threading.Event()
                otp_thread = threading.Thread(target=realtime_otp_worker, args=(stop_event,), daemon=True)
                otp_thread.start()

                success_count = 0
                attempts = 0
                while success_count < count and attempts < (count * 3):
                    attempts += 1
                    num = fetch_api_number(rid=selected_rid)
                    if not num:
                        time.sleep(0.3)
                        continue
                    
                    formatted_num = f"+{num}" if not str(num).startswith("+") else str(num)
                    check_status = check_number_graphql(formatted_num)
                    
                    if check_status == 'taken':
                        continue
                    
                    process_number(number=num, password=password, bot_instance=bot, chat_id=chat_id, user_info=user_info, rid=selected_rid)
                    success_count += 1
                    time.sleep(0.3)

                start_w = time.time()
                while time.time() - start_w < 1800:
                    with counter_lock:
                        pending = [a for a in SUCCESSFUL_ACCOUNTS_LOG if a["otp"] in ["PENDING", "------"]]
                    if not pending:
                        break
                    time.sleep(1)

                stop_event.set()
                bot.send_message(chat_id, f"✅ সমস্ত অ্যাকাউন্ট তৈরি এবং লাইভ OTP প্রসেসিং সফলভাবে সম্পূর্ণ হয়েছে!", reply_markup=main_menu_keyboard())

            threading.Thread(target=run_bot_process).start()
            user_sessions[chat_id] = {'step': 'waiting_count'}

    @bot.callback_query_handler(func=lambda call: call.data.startswith('rid_'))
    def callback_query_range(call):
        chat_id = call.message.chat.id
        try:
            idx = int(call.data.split('_')[1])
            state = user_sessions.get(chat_id, {})
            ranges = state.get('ranges', get_live_ranges_from_api())
            
            if 0 <= idx < len(ranges):
                selected_range = ranges[idx]
                state['rid'] = selected_range['id']
                state['step'] = 'waiting_count'
                user_sessions[chat_id] = state
                
                bot.answer_callback_query(call.id, f"Selected: {selected_range['country']}")
                bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=call.message.message_id,
                    text=f"✅ সিলেক্টেড রেইঞ্জ:\n🌍 *দেশ:* `{selected_range['country']}`\n📌 *RID:* `{selected_range['id']}`\n⚡ *ট্রাফিক:* `{selected_range['traffic']}`\n\n🔢 এখন কয়টি সচল অ্যাকাউন্ট তৈরি করতে চান সংখ্যাটি লিখুন (যেমন: 5):",
                    parse_mode='Markdown'
                )
            else:
                bot.answer_callback_query(call.id, "❌ Invalid range selected!")
        except Exception as e:
            bot.answer_callback_query(call.id, f"❌ Error: {str(e)[:30]}")

    print(f"{GREEN}[*] Telegram Bot v4.5 PRO is running...{RST}")
    bot.infinity_polling()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    clear_logo()
    global USER_PASSWORD

    print(f"{GREEN} [1] Run with Number_List.txt (File Mode){RST}")
    print(f"{GREEN} [2] Run with Auto API & Fast Batch Creation{RST}")
    print(f"{GREEN} [3] ⚡ Live Traffic & Ranges Monitor (Real-Time Auto-Refresh){RST}")
    print(f"{GREEN} [4] View Global Live Feed (Console){RST}")
    print(f"{GREEN} [5] Run as Telegram Bot{RST}")
    choice = input(f"\n{GREEN} Select Option [1/2/3/4/5] {EKL} {WHITE}").strip()

    if choice == '5':
        start_telegram_bot()
        return
    elif choice == '3':
        live_traffic_ranges_monitor()
        main()
        return
    elif choice == '4':
        print(f"\n{CYAN}[*] Fetching Global Live Console Feed...{RST}")
        res = fetch_console_feed()
        print(json.dumps(res, indent=2) if isinstance(res, (dict, list)) else res)
        input(f"\n{WHITE} Press Enter to exit...{RST}")
        return

    pwd_input = input(f"{GREEN}{BOLD} [{PINK}●{GREEN}] Enter Password {GREEN}(Enter=Default){EKL} {WHITE}").strip()
    if pwd_input: USER_PASSWORD = pwd_input

    numbers = []
    
    if choice == '2':
        print(f"\n{GREEN} [*] Fetching live traffic ranges from Voltx panel...{RST}")
        fetched_ranges = get_live_ranges_from_api()
        
        print(f"\n{GREEN}{BOLD}FACEBOOK - ACTIVE LIVE TRAFFIC RANGES ({len(fetched_ranges)}){RST}")
        print(LINE)
        for idx, r in enumerate(fetched_ranges, 1):
            print(f" {GREEN}[{idx}]{RST} {WHITE}RID: {r['id']} {GREEN}---{RST} {WHITE}{r['country']} ({r['code']}) [{YELLOW}{r['traffic']}{WHITE}]{RST}")
        print(LINE)

        sel = input(f"{GREEN} SELECT RANGE [1-{len(fetched_ranges)}] {EKL} {WHITE}").strip()
        selected_rid = DEFAULT_RID
        try:
            s_idx = int(sel)
            if 1 <= s_idx <= len(fetched_ranges):
                selected_rid = fetched_ranges[s_idx - 1]["id"]
        except:
            pass

        print(f"{CYAN} [*] Selected Live Range ID: {selected_rid}{RST}")

        try:
            count_input = input(f"{GREEN} [{RED}●{GREEN}] How many fresh accounts to create? {EKL} {WHITE}").strip()
            total_to_fetch = int(count_input) if count_input else 5
        except:
            total_to_fetch = 5

        print(f"{GREEN} [*] Starting Fast Batch Creation loop using live range {selected_rid}...{RST}")
        
        stop_event = threading.Event()
        otp_thread = threading.Thread(target=realtime_otp_worker, args=(stop_event,), daemon=True)
        otp_thread.start()

        created_count = 0
        attempts = 0
        while created_count < total_to_fetch and attempts < (total_to_fetch * 3):
            attempts += 1
            num = fetch_api_number(rid=selected_rid)
            if not num:
                time.sleep(0.3)
                continue
            
            formatted_num = f"+{num}" if not str(num).startswith("+") else str(num)
            check_status = check_number_graphql(formatted_num)
            
            if check_status == 'taken':
                print(f"{YELLOW} [-] Number {formatted_num} is Taken. Skipping...{RST}")
                continue
            
            print(f"{GREEN} [+] Number {formatted_num} is Free! Creating account...{RST}")
            process_number(number=num, password=USER_PASSWORD, proxy=None, bot_instance=None, chat_id=None, user_info=None, rid=selected_rid)
            created_count += 1
            time.sleep(0.3)
        
        display_final_summary()
        stop_event.set()
        input(f"\n{WHITE} Press Enter to exit...{RST}")
        return
    else:
        phone_file = input(f"{GREEN} [{RED}●{RED}]{RST} {GREEN}Phone File {GREEN}(Enter=Number_List.txt){RST}{EKL} {WHITE}").strip()
        if not phone_file: phone_file = 'Number_List.txt'

        print(f"\n{LINE}")
        print(f"{GREEN}{BOLD}   SESSION INFO (v4.5 ULTRA STRONG + REAL-TIME OTP){RST}")
        print(LINE)
        print(f"{GREEN} Developer {EKL} {WHITE}@O_J_A_N_T_H_A")
        print(f"{GREEN} Password  {EKL} {GREEN}{USER_PASSWORD}")
        print(LINE)

        input(f"{GREEN} Press Enter to Start...{RST}")
        return

if __name__ == "__main__":
    main()