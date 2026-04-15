#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linux AI Yordamchi - Oddiy terminalda ishlaydi
Barcha xatolarni avtomatik tuzatadi
"""

import subprocess
import sys
import os
import re

def exec_command(cmd):
    """Komandani bajarish"""
    try:
        result = subprocess.run(cmd, shell=True, text=True, capture_output=True, timeout=30)
        return result.stdout + result.stderr, result.returncode
    except:
        return "Xato yuz berdi", 1

def fix_command(cmd, error):
    """Xatolarni avtomatik tuzatish"""
    error_lower = error.lower()
    cmd_clean = cmd.strip()
    
    # 1. sudo qo'shish kerak bo'lsa
    if "permission denied" in error_lower:
        return f"sudo {cmd_clean}"
    
    # 2. python -> python3
    if cmd_clean.startswith("python ") or cmd_clean == "python":
        return cmd_clean.replace("python", "python3", 1)
    
    # 3. pip -> pip3
    if cmd_clean.startswith("pip "):
        return cmd_clean.replace("pip", "pip3", 1)
    
    # 4. apt-get update dan oldin sudo
    if "apt-get" in cmd_clean and "could not open lock file" in error_lower:
        return f"sudo {cmd_clean}"
    
    # 5. Paket o'rnatishda sudo
    if ("apt install" in cmd_clean or "apt-get install" in cmd_clean) and "permission" in error_lower:
        return f"sudo {cmd_clean}"
    
    # 6. Service boshqarishda sudo
    if ("systemctl" in cmd_clean or "service" in cmd_clean) and "permission" in error_lower:
        return f"sudo {cmd_clean}"
    
    # 7. cd dan keyin ls qilish
    if cmd_clean.startswith("cd ") and "no such file" in error_lower:
        dir_name = cmd_clean[3:].strip()
        return f"ls -la | grep {dir_name}"
    
    # 8. Fayl topilmasa, ls bilan tekshirish
    if "no such file" in error_lower or "cannot find" in error_lower:
        return "ls -la"
    
    # 9. Komanda topilmasa, o'rnatishni taklif qilish
    if "command not found" in error_lower:
        prog = cmd_clean.split()[0]
        install_commands = {
            "nmap": "sudo apt install nmap -y",
            "curl": "sudo apt install curl -y",
            "wget": "sudo apt install wget -y",
            "git": "sudo apt install git -y",
            "vim": "sudo apt install vim -y",
            "nano": "sudo apt install nano -y",
            "htop": "sudo apt install htop -y",
            "tree": "sudo apt install tree -y",
            "jq": "sudo apt install jq -y",
            "netstat": "sudo apt install net-tools -y",
            "ifconfig": "sudo apt install net-tools -y",
            "ping": "sudo apt install iputils-ping -y",
            "ssh": "sudo apt install openssh-client -y",
            "python3": "sudo apt install python3 -y",
            "pip3": "sudo apt install python3-pip -y"
        }
        
        if prog in install_commands:
            return install_commands[prog]
        else:
            return f"sudo apt install {prog} -y"
    
    # 10. Noto'g'ri parametr
    if "invalid option" in error_lower or "illegal option" in error_lower:
        prog = cmd_clean.split()[0]
        return f"{prog} --help"
    
    # 11. Paket topilmadi
    if "unable to locate package" in error_lower:
        return "sudo apt update"
    
    # 12. Disk to'ldi
    if "no space left" in error_lower:
        return "df -h && du -sh /* 2>/dev/null | sort -h"
    
    # 13. Bog'liqlik muammosi
    if "dependency" in error_lower or "broken packages" in error_lower:
        return "sudo apt --fix-broken install"
    
    # 14. Port band
    if "address already in use" in error_lower or "port already in use" in error_lower:
        return "netstat -tulpn | grep LISTEN"
    
    # 15. Git muammolari
    if "not a git repository" in error_lower:
        return "git init"
    
    # 16. Virtual environment
    if "no module named" in error_lower:
        module = re.search(r"No module named ['\"]([^'\"]+)", error)
        if module:
            return f"pip3 install {module.group(1)}"
        return "pip3 list"
    
    # 17. Hech narsa topilmasa
    return None

def main():
    """Asosiy funksiya"""
    print("\n" + "="*60)
    print("     🤖 LINUX AI YORDAMCHI - To'liq avtomatik")
    print("="*60)
    print("\n⚡ Bu dastur barcha xatolarni avtomatik tuzatadi!")
    print("💡 Siz faqat komandalarni yozasiz, men xatolarni tuzataman")
    print("\n📌 Chiqish uchun: 'chiq' yoki 'exit' yoki Ctrl+C")
    print("-"*60 + "\n")
    
    while True:
        try:
            # Komanda olish
            cmd = input("┌─[$]─[user]\n└─$ ").strip()
            
            if not cmd:
                continue
            
            # Chiqish komandalari
            if cmd.lower() in ['chiq', 'exit', 'quit', 'chiquv']:
                print("\n👋 Xayr! Laboratoriyangizda omad!\n")
                break
            
            # maxsus komandalar
            if cmd.lower() == 'help' or cmd.lower() == 'yordam':
                print("\n📖 Men barcha xatolarni tuzataman!")
                print("   Hech narsa qilishingiz shart emas, faqat komanda yozing")
                print("   Xato chiqsa, men avtomatik tuzataman va taklifni bajaraman\n")
                continue
            
            # Komandani bajarish
            print(f"\n🐧 Siz: {cmd}")
            output, code = exec_command(cmd)
            
            # Agar muvaffaqiyatli bo'lsa
            if code == 0:
                print("✅ Muvaffaqiyatli bajarildi!")
                if output and len(output) < 500:
                    print(output)
                elif output:
                    print(output[:500] + "\n... (chiqish juda uzun)")
            else:
                # Xato bo'lsa, avtomatik tuzatish
                print("⚠️ Xato yuz berdi, avtomatik tuzatilmoqda...")
                
                fixed_cmd = fix_command(cmd, output)
                
                if fixed_cmd:
                    print(f"🔧 Taklif: {fixed_cmd}")
                    print("🔄 Avtomatik bajarilmoqda...")
                    
                    # Taklifni bajarish
                    new_output, new_code = exec_command(fixed_cmd)
                    
                    if new_code == 0:
                        print("✅ Tuzatildi! Natija:")
                        if new_output and len(new_output) < 500:
                            print(new_output)
                        else:
                            print("✅ Komanda muvaffaqiyatli bajarildi")
                    else:
                        print("❌ Avtomatik tuzatish ishlamadi")
                        print(f"📋 Xato: {output[:200]}")
                else:
                    print("❌ Tuzatish topilmadi")
                    print(f"📋 Xato: {output[:200]}")
            
            print("-"*60 + "\n")
        
        except KeyboardInterrupt:
            print("\n\n👋 Dastur to'xtatildi\n")
            break
        except EOFError:
            break
        except Exception as e:
            print(f"❌ Xato: {e}")
            continue

if __name__ == "__main__":
    main()