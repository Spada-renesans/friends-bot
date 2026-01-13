{\rtf1\ansi\ansicpg1251\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
from datetime import datetime, timedelta\
from supabase import create_client\
from telegram import Update\
from telegram.ext import Application, MessageHandler, filters, ContextTypes\
from dotenv import load_dotenv\
\
# \uc0\u1047 \u1072 \u1075 \u1088 \u1091 \u1078 \u1072 \u1077 \u1084  \u1087 \u1077 \u1088 \u1077 \u1084 \u1077 \u1085 \u1085 \u1099 \u1077  \u1086 \u1082 \u1088 \u1091 \u1078 \u1077 \u1085 \u1080 \u1103 \
load_dotenv()\
\
# \uc0\u1053 \u1072 \u1089 \u1090 \u1088 \u1086 \u1081 \u1082 \u1080 \
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")\
SUPABASE_URL = os.getenv("SUPABASE_URL")\
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")\
\
# \uc0\u1055 \u1088 \u1086 \u1074 \u1077 \u1088 \u1103 \u1077 \u1084  \u1095 \u1090 \u1086  \u1074 \u1089 \u1077  \u1076 \u1072 \u1085 \u1085 \u1099 \u1077  \u1077 \u1089 \u1090 \u1100 \
if not BOT_TOKEN or not SUPABASE_URL or not SUPABASE_KEY:\
    print("\uc0\u10060  \u1054 \u1064 \u1048 \u1041 \u1050 \u1040 : \u1053 \u1077  \u1079 \u1072 \u1087 \u1086 \u1083 \u1085 \u1077 \u1085 \u1099  \u1087 \u1077 \u1088 \u1077 \u1084 \u1077 \u1085 \u1085 \u1099 \u1077  \u1074  .env \u1092 \u1072 \u1081 \u1083 \u1077 !")\
    print("\uc0\u1055 \u1088 \u1086 \u1074 \u1077 \u1088 \u1100 : TELEGRAM_BOT_TOKEN, SUPABASE_URL, SUPABASE_ANON_KEY")\
    exit(1)\
\
# \uc0\u1055 \u1086 \u1076 \u1082 \u1083 \u1102 \u1095 \u1077 \u1085 \u1080 \u1077  \u1082  Supabase\
try:\
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)\
    print("\uc0\u9989  \u1055 \u1086 \u1076 \u1082 \u1083 \u1102 \u1095 \u1077 \u1085 \u1080 \u1077  \u1082  Supabase \u1091 \u1089 \u1087 \u1077 \u1096 \u1085 \u1086 !")\
except Exception as e:\
    print(f"\uc0\u10060  \u1054 \u1096 \u1080 \u1073 \u1082 \u1072  \u1087 \u1086 \u1076 \u1082 \u1083 \u1102 \u1095 \u1077 \u1085 \u1080 \u1103  \u1082  Supabase: \{e\}")\
    exit(1)\
\
# \uc0\u1053 \u1072 \u1089 \u1090 \u1088 \u1086 \u1081 \u1082 \u1080  \u1073 \u1086 \u1090 \u1072 \
BOT_NAME = "\uc0\u1050 \u1086 \u1088 \u1077 \u1096 "\
PERSONALITY = "\uc0\u1082 \u1088 \u1072 \u1090 \u1082 \u1080 \u1081 , \u1073 \u1077 \u1079  \u1074 \u1086 \u1076 \u1099 , \u1086 \u1090 \u1074 \u1077 \u1095 \u1072 \u1077 \u1090  \u1090 \u1086 \u1083 \u1100 \u1082 \u1086  \u1087 \u1086  \u1076 \u1077 \u1083 \u1091 "\
\
# \uc0\u1050 \u1083 \u1102 \u1095 \u1077 \u1074 \u1099 \u1077  \u1089 \u1083 \u1086 \u1074 \u1072  \u1076 \u1083 \u1103  \u1072 \u1082 \u1090 \u1080 \u1074 \u1072 \u1094 \u1080 \u1080 \
TRIGGER_WORDS = \{\
    'banya': ['\uc0\u1073 \u1072 \u1085 \u1080 ', '\u1073 \u1072 \u1085 \u1103 ', '\u1074 \u1077 \u1085 \u1080 \u1082 ', '\u1087 \u1072 \u1088 ', '\u1084 \u1099 \u1083 \u1086 ', '\u1084 \u1099 \u1090 \u1100 \u1089 \u1103 ', '\u1095 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 '],\
    'fishing': ['\uc0\u1088 \u1099 \u1073 \u1072 \u1083 \u1082 \u1072 ', '\u1088 \u1099 \u1073 \u1072 ', '\u1091 \u1076 \u1086 \u1095 \u1082 \u1072 ', '\u1083 \u1077 \u1089 \u1082 \u1072 ', '\u1082 \u1088 \u1102 \u1095 \u1086 \u1082 '],\
    'mushrooms': ['\uc0\u1075 \u1088 \u1080 \u1073 ', '\u1075 \u1088 \u1080 \u1073 \u1099 ', '\u1082 \u1086 \u1088 \u1079 \u1080 \u1085 \u1072 ', '\u1083 \u1077 \u1089 '],\
    'trip': ['\uc0\u1087 \u1086 \u1077 \u1079 \u1076 \u1082 \u1072 ', '\u1077 \u1093 \u1072 \u1090 \u1100 ', '\u1084 \u1072 \u1096 \u1080 \u1085 \u1072 ', '\u1087 \u1086 \u1077 \u1093 \u1072 \u1083 \u1080 ']\
\}\
\
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    """\uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1072 \u1090 \u1099 \u1074 \u1072 \u1077 \u1090  \u1089 \u1086 \u1086 \u1073 \u1097 \u1077 \u1085 \u1080 \u1103  \u1073 \u1077 \u1079  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076 """\
    \
    if not update.message or not update.message.text:\
        return\
    \
    text = update.message.text.lower()\
    user = update.message.from_user\
    chat_id = update.message.chat_id\
    \
    print(f"\uc0\u55357 \u56553  \u1057 \u1086 \u1086 \u1073 \u1097 \u1077 \u1085 \u1080 \u1077  \u1086 \u1090  @\{user.username or 'unknown'\}: \{update.message.text\}")\
    \
    # \uc0\u1055 \u1088 \u1086 \u1074 \u1077 \u1088 \u1103 \u1077 \u1084  - \u1101 \u1090 \u1086  \u1087 \u1088 \u1086  \u1085 \u1072 \u1096 \u1080  \u1090 \u1077 \u1084 \u1099 ?\
    context_type = None\
    for topic, keywords in TRIGGER_WORDS.items():\
        if any(kw in text for kw in keywords):\
            context_type = topic\
            break\
    \
    # \uc0\u1045 \u1089 \u1083 \u1080  \u1085 \u1077  \u1087 \u1088 \u1086  \u1085 \u1072 \u1096 \u1080  \u1090 \u1077 \u1084 \u1099  - \u1080 \u1075 \u1085 \u1086 \u1088 \u1080 \u1088 \u1091 \u1077 \u1084 \
    if not context_type:\
        return\
    \
    # \uc0\u1045 \u1089 \u1083 \u1080  \u1087 \u1083 \u1102 \u1089 \u1080 \u1082  \u1074  \u1082 \u1086 \u1085 \u1090 \u1077 \u1082 \u1089 \u1090 \u1077  \u1073 \u1072 \u1085 \u1080  - \u1079 \u1072 \u1087 \u1080 \u1089 \u1099 \u1074 \u1072 \u1077 \u1084 \
    if '+' in text and context_type == 'banya':\
        await handle_plus_sign(update, context)\
        return\
    \
    # \uc0\u1043 \u1077 \u1085 \u1077 \u1088 \u1080 \u1088 \u1091 \u1077 \u1084  \u1086 \u1090 \u1074 \u1077 \u1090  \u1087 \u1086  \u1082 \u1086 \u1085 \u1090 \u1077 \u1082 \u1089 \u1090 \u1091 \
    response = generate_response(text, context_type, user)\
    \
    if response:\
        try:\
            await update.message.reply_text(response)\
            print(f"\uc0\u9989  \u1054 \u1090 \u1074 \u1077 \u1090  \u1086 \u1090 \u1087 \u1088 \u1072 \u1074 \u1083 \u1077 \u1085 : \{response\}")\
            \
            # \uc0\u1057 \u1086 \u1093 \u1088 \u1072 \u1085 \u1103 \u1077 \u1084  \u1074  \u1087 \u1072 \u1084 \u1103 \u1090 \u1100 \
            save_to_memory(chat_id, 'user', text, context_type)\
            save_to_memory(chat_id, 'assistant', response, context_type)\
        except Exception as e:\
            print(f"\uc0\u10060  \u1054 \u1096 \u1080 \u1073 \u1082 \u1072  \u1086 \u1090 \u1087 \u1088 \u1072 \u1074 \u1082 \u1080 : \{e\}")\
\
async def handle_plus_sign(update, context):\
    """\uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1072 \u1090 \u1099 \u1074 \u1072 \u1077 \u1090  + \u1076 \u1083 \u1103  \u1079 \u1072 \u1087 \u1080 \u1089 \u1080  \u1085 \u1072  \u1073 \u1072 \u1085 \u1102 """\
    user = update.message.from_user\
    chat_id = update.message.chat_id\
    \
    print(f"\uc0\u55357 \u56541  \u1047 \u1072 \u1087 \u1080 \u1089 \u1100  \u1085 \u1072  \u1073 \u1072 \u1085 \u1102 : \{user.first_name\}")\
    \
    try:\
        # \uc0\u1055 \u1086 \u1083 \u1091 \u1095 \u1072 \u1077 \u1084  \u1080 \u1083 \u1080  \u1089 \u1086 \u1079 \u1076 \u1072 \u1077 \u1084  \u1089 \u1086 \u1073 \u1099 \u1090 \u1080 \u1077  \u1073 \u1072 \u1085 \u1080 \
        next_thursday = get_next_banya_date()\
        \
        # \uc0\u1048 \u1097 \u1077 \u1084  \u1089 \u1086 \u1073 \u1099 \u1090 \u1080 \u1077  \u1085 \u1072  \u1101 \u1090 \u1086 \u1090  \u1095 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 \
        events = supabase.table('events').select('*').eq('event_type', 'banya').eq('event_date', next_thursday.isoformat()).execute()\
        \
        if not events.data:\
            # \uc0\u1057 \u1086 \u1079 \u1076 \u1072 \u1077 \u1084  \u1089 \u1086 \u1073 \u1099 \u1090 \u1080 \u1077 \
            event = supabase.table('events').insert(\{\
                'event_type': 'banya',\
                'event_date': next_thursday.isoformat(),\
                'description': '\uc0\u1045 \u1078 \u1077 \u1085 \u1077 \u1076 \u1077 \u1083 \u1100 \u1085 \u1072 \u1103  \u1073 \u1072 \u1085 \u1103 '\
            \}).execute()\
            event_id = event.data[0]['id']\
        else:\
            event_id = events.data[0]['id']\
        \
        # \uc0\u1047 \u1072 \u1087 \u1080 \u1089 \u1099 \u1074 \u1072 \u1077 \u1084  \u1091 \u1095 \u1072 \u1089 \u1090 \u1085 \u1080 \u1082 \u1072 \
        supabase.table('participants').upsert(\{\
            'event_id': event_id,\
            'user_id': user.id,\
            'username': user.username,\
            'first_name': user.first_name,\
            'is_drinking': False\
        \}).execute()\
        \
        # \uc0\u1055 \u1086 \u1083 \u1091 \u1095 \u1072 \u1077 \u1084  \u1089 \u1087 \u1080 \u1089 \u1086 \u1082  \u1091 \u1095 \u1072 \u1089 \u1090 \u1085 \u1080 \u1082 \u1086 \u1074 \
        participants = get_participants(event_id)\
        names = [p['first_name'] or p['username'] or '\uc0\u1040 \u1085 \u1086 \u1085 \u1080 \u1084 ' for p in participants]\
        \
        response = f"\uc0\u9989  \{user.first_name or user.username\} \u1079 \u1072 \u1087 \u1080 \u1089 \u1072 \u1085 !\\n" \\\
                  f"\uc0\u55358 \u56790  \u1048 \u1076 \u1077 \u1090 : \{len(participants)\} \u1095 \u1077 \u1083 \u1086 \u1074 \u1077 \u1082 \\n" \\\
                  f"\uc0\u55357 \u56421  \{', '.join(names)\}"\
        \
        await update.message.reply_text(response)\
        print(f"\uc0\u9989  \u1047 \u1072 \u1087 \u1080 \u1089 \u1100  \u1091 \u1089 \u1087 \u1077 \u1096 \u1085 \u1072 : \{len(participants)\} \u1091 \u1095 \u1072 \u1089 \u1090 \u1085 \u1080 \u1082 \u1086 \u1074 ")\
        \
    except Exception as e:\
        print(f"\uc0\u10060  \u1054 \u1096 \u1080 \u1073 \u1082 \u1072  \u1079 \u1072 \u1087 \u1080 \u1089 \u1080 : \{e\}")\
        await update.message.reply_text(f"\uc0\u55357 \u56853  \u1054 \u1096 \u1080 \u1073 \u1082 \u1072 : \{str(e)\}")\
\
def get_participants(event_id):\
    """\uc0\u1055 \u1086 \u1083 \u1091 \u1095 \u1072 \u1077 \u1090  \u1089 \u1087 \u1080 \u1089 \u1086 \u1082  \u1091 \u1095 \u1072 \u1089 \u1090 \u1085 \u1080 \u1082 \u1086 \u1074 """\
    try:\
        result = supabase.table('participants').select('*').eq('event_id', event_id).execute()\
        return result.data or []\
    except Exception as e:\
        print(f"\uc0\u10060  \u1054 \u1096 \u1080 \u1073 \u1082 \u1072  \u1087 \u1086 \u1083 \u1091 \u1095 \u1077 \u1085 \u1080 \u1103  \u1091 \u1095 \u1072 \u1089 \u1090 \u1085 \u1080 \u1082 \u1086 \u1074 : \{e\}")\
        return []\
\
def generate_response(text, context_type, user):\
    """\uc0\u1043 \u1077 \u1085 \u1077 \u1088 \u1080 \u1088 \u1091 \u1077 \u1090  \u1086 \u1090 \u1074 \u1077 \u1090  \u1087 \u1086  \u1082 \u1086 \u1085 \u1090 \u1077 \u1082 \u1089 \u1090 \u1091 """\
    \
    context_names = \{\
        'banya': '\uc0\u1073 \u1072 \u1085 \u1080 ',\
        'fishing': '\uc0\u1088 \u1099 \u1073 \u1072 \u1083 \u1082 \u1080 ',\
        'mushrooms': '\uc0\u1075 \u1088 \u1080 \u1073 \u1086 \u1074 ',\
        'trip': '\uc0\u1087 \u1086 \u1077 \u1079 \u1076 \u1082 \u1080 '\
    \}\
    \
    if context_type == 'banya':\
        if '\uc0\u1089 \u1082 \u1086 \u1083 \u1100 \u1082 \u1086 ' in text or '\u1082 \u1090 \u1086 ' in text:\
            participants = get_current_banya_participants()\
            names = [p['first_name'] or p['username'] or '\uc0\u1040 \u1085 \u1086 \u1085 \u1080 \u1084 ' for p in participants]\
            if names:\
                return f"\uc0\u55358 \u56790  \u1053 \u1072  \u1073 \u1072 \u1085 \u1102  \u1080 \u1076 \u1091 \u1090 : \{', '.join(names)\} (\{len(participants)\} \u1095 \u1077 \u1083 )"\
            else:\
                return "\uc0\u55358 \u56790  \u1055 \u1086 \u1082 \u1072  \u1085 \u1080 \u1082 \u1090 \u1086  \u1085 \u1077  \u1079 \u1072 \u1087 \u1080 \u1089 \u1072 \u1085 . \u1055 \u1080 \u1096 \u1080 \u1090 \u1077  +"\
        \
        if '\uc0\u1082 \u1086 \u1075 \u1076 \u1072 ' in text:\
            next_thursday = get_next_banya_date()\
            return f"\uc0\u55357 \u56517  \u1041 \u1072 \u1085 \u1103 : \{next_thursday.strftime('%d.%m')\}, \u1095 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 "\
        \
        if '\uc0\u1084 \u1080 \u1085 \u1091 \u1089 ' in text or '-' in text:\
            try:\
                next_thursday = get_next_banya_date()\
                events = supabase.table('events').select('*').eq('event_type', 'banya').eq('event_date', next_thursday.isoformat()).execute()\
                if events.data:\
                    supabase.table('participants').delete().eq('event_id', events.data[0]['id']).eq('user_id', user.id).execute()\
                    return f"\uc0\u10060  \{user.first_name or user.username\} \u1086 \u1090 \u1087 \u1080 \u1089 \u1072 \u1085 "\
            except:\
                pass\
    \
    elif context_type == 'fishing':\
        if '\uc0\u1082 \u1086 \u1075 \u1076 \u1072 ' in text:\
            return "\uc0\u55356 \u57251  \u1053 \u1072  \u1088 \u1099 \u1073 \u1072 \u1083 \u1082 \u1091  \u1074  \u1089 \u1091 \u1073 \u1073 \u1086 \u1090 \u1091  \u1089  \u1091 \u1090 \u1088 \u1072 !"\
        if '\uc0\u1075 \u1076 \u1077 ' in text:\
            return "\uc0\u55356 \u57251  \u1053 \u1072  \u1085 \u1072 \u1096 \u1077 \u1084  \u1084 \u1077 \u1089 \u1090 \u1077 "\
    \
    elif context_type == 'mushrooms':\
        if '\uc0\u1075 \u1076 \u1077 ' in text:\
            return "\uc0\u55356 \u57156  \u1042  \u1083 \u1077 \u1089  \u1079 \u1072  30\u1082 \u1084 "\
        if '\uc0\u1082 \u1086 \u1075 \u1076 \u1072 ' in text:\
            return "\uc0\u55356 \u57156  \u1057 \u1091 \u1073 \u1073 \u1086 \u1090 \u1072  \u1091 \u1090 \u1088 \u1086 \u1084 "\
    \
    elif context_type == 'trip':\
        if '\uc0\u1082 \u1091 \u1076 \u1072 ' in text or '\u1075 \u1076 \u1077 ' in text:\
            return "\uc0\u55357 \u56983  \u1054 \u1073 \u1089 \u1091 \u1076 \u1080 \u1084 "\
    \
    # \uc0\u1050 \u1088 \u1072 \u1090 \u1082 \u1080 \u1077  \u1088 \u1077 \u1072 \u1082 \u1094 \u1080 \u1080 \
    emoji_map = \{'banya': '\uc0\u55358 \u56790 ', 'fishing': '\u55356 \u57251 ', 'mushrooms': '\u55356 \u57156 ', 'trip': '\u55357 \u56983 '\}\
    emoji = emoji_map.get(context_type, '\uc0\u55357 \u56397 ')\
    return f"\{emoji\} \{context_names.get(context_type, context_type)\}"\
\
def save_to_memory(chat_id, role, content, context_type):\
    """\uc0\u1057 \u1086 \u1093 \u1088 \u1072 \u1085 \u1103 \u1077 \u1090  \u1089 \u1086 \u1086 \u1073 \u1097 \u1077 \u1085 \u1080 \u1077  \u1074  \u1087 \u1072 \u1084 \u1103 \u1090 \u1100 """\
    try:\
        supabase.table('chat_memory').insert(\{\
            'chat_id': chat_id,\
            'role': role,\
            'content': content,\
            'context': context_type\
        \}).execute()\
    except Exception as e:\
        print(f"\uc0\u10060  \u1054 \u1096 \u1080 \u1073 \u1082 \u1072  \u1089 \u1086 \u1093 \u1088 \u1072 \u1085 \u1077 \u1085 \u1080 \u1103  \u1074  \u1087 \u1072 \u1084 \u1103 \u1090 \u1100 : \{e\}")\
\
def get_next_banya_date():\
    """\uc0\u1042 \u1086 \u1079 \u1074 \u1088 \u1072 \u1097 \u1072 \u1077 \u1090  \u1076 \u1072 \u1090 \u1091  \u1089 \u1083 \u1077 \u1076 \u1091 \u1102 \u1097 \u1077 \u1075 \u1086  \u1095 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 \u1072 """\
    today = datetime.now().date()\
    days_until_thursday = (3 - today.weekday()) % 7\
    if days_until_thursday == 0:\
        days_until_thursday = 7\
    return today + timedelta(days=days_until_thursday)\
\
def get_current_banya_participants():\
    """\uc0\u1055 \u1086 \u1083 \u1091 \u1095 \u1072 \u1077 \u1090  \u1091 \u1095 \u1072 \u1089 \u1090 \u1085 \u1080 \u1082 \u1086 \u1074  \u1085 \u1072  \u1073 \u1083 \u1080 \u1078 \u1072 \u1081 \u1096 \u1091 \u1102  \u1073 \u1072 \u1085 \u1102 """\
    try:\
        next_thursday = get_next_banya_date()\
        events = supabase.table('events').select('*').eq('event_type', 'banya').eq('event_date', next_thursday.isoformat()).execute()\
        \
        if events.data:\
            return get_participants(events.data[0]['id'])\
        return []\
    except Exception as e:\
        print(f"\uc0\u10060  \u1054 \u1096 \u1080 \u1073 \u1082 \u1072 : \{e\}")\
        return []\
\
def main():\
    """\uc0\u1047 \u1072 \u1087 \u1091 \u1089 \u1082  \u1073 \u1086 \u1090 \u1072 """\
    print("="*50)\
    print(f"\uc0\u55358 \u56598  \u1047 \u1072 \u1087 \u1091 \u1089 \u1082  \u1073 \u1086 \u1090 \u1072 : \{BOT_NAME\}")\
    print(f"\uc0\u55357 \u56522  Personality: \{PERSONALITY\}")\
    print("="*50)\
    \
    app = Application.builder().token(BOT_TOKEN).build()\
    \
    # \uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1072 \u1090 \u1099 \u1074 \u1072 \u1077 \u1084  \u1074 \u1089 \u1077  \u1090 \u1077 \u1082 \u1089 \u1090 \u1086 \u1074 \u1099 \u1077  \u1089 \u1086 \u1086 \u1073 \u1097 \u1077 \u1085 \u1080 \u1103  \u1073 \u1077 \u1079  \u1082 \u1086 \u1084 \u1072 \u1085 \u1076 \
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))\
    \
    print("\uc0\u9989  \u1041 \u1086 \u1090  \u1079 \u1072 \u1087 \u1091 \u1097 \u1077 \u1085  \u1080  \u1089 \u1083 \u1091 \u1096 \u1072 \u1077 \u1090  \u1089 \u1086 \u1086 \u1073 \u1097 \u1077 \u1085 \u1080 \u1103 ...")\
    print("\uc0\u55357 \u56395  \u1053 \u1072 \u1087 \u1080 \u1096 \u1080  \u1095 \u1090 \u1086 -\u1090 \u1086  \u1074  \u1095 \u1072 \u1090 !")\
    \
    app.run_polling()\
\
if __name__ == '__main__':\
    main()\
}