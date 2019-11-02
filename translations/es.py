"""
This module contains the result sentences and intents for the French version
of the Assistant information app.
"""

# Result sentences
RESULT_ASSISTANT_APPS = "Tengo {} aplicaciones : {}."
RESULT_ASSISTANT_ID = "Mi identificación es : {}."
RESULT_ASSISTANT_INTENTS = "Puedo comprender estas {} peticiones."
RESULT_ASSISTANT_NAME = "Mi nombre es {}."
RESULT_ASSISTANT_PLATFORM = "Funciono en la plataforma {}."
RESULT_HOSTNAME = "Mi host es {}."
RESULT_IP_ADDRESS = "Mi dirección IP es {}."
RESULT_SNIPS_VERSION = "Uso la versión {} de Snips."
RESULT_NEWER_VERSION_AVAILABLE = "Hay una nueva versión de Snips disponible."
RESULT_LATEST_SNIPS_VERSION = "La última versión de Snips es {}."
RESULT_OLDER = "Uso una versión antigua de Snips. Podría actualizarme."
RESULT_NO_RELEASE_NOTES = "Lo siento, No puedo acceder a las versiones de Snips."
RESULT_UPDATED = "Ya estoy en la última versión de Snips, es la {}."
RESULT_NOT_UPDATED = "Permanezco en la versión {} de Snips, y la versión {} está disponible."
RESULT_UPTIME = "Ya he iniciado {}."
AND = ", y "

# TTS workarounds
REPLACE_TTS_RASPI = "Raspberry Pi"

def tts_ip_address(ip_address):
    """Convert an IP address to something the TTS will pronounce correctly.

    Args:
        ip_address (str): The IP address, e.g. '102.168.0.102'

    Returns:
        str: A pronounceable IP address, e.g. '192 dot 168 dot 0 dot 102'
    """
    return ip_address.replace('.', ' punto ')

def tts_version(version):
    """Convert a version string to something the TTS will pronounce correctly.

    Args:
        version (str): The version string, e.g. '1.1.2'

    Returns:
        str: A pronounceable version string, e.g. '1 point 1 point 2'
    """
    return version.replace('.', ' punto ')

# Intents
INTENT_ASSISTANT_APPS = 'SparkMonkey:AssistantApps'
INTENT_ASSISTANT_ID = 'SparkMonkey:AssistantID'
INTENT_ASSISTANT_INTENTS = 'SparkMonkey:AssistantIntents'
INTENT_ASSISTANT_NAME = 'SparkMonkey:AssistantName'
INTENT_ASSISTANT_PLATFORM = 'SparkMonkey:AssistantPlatform'
INTENT_HOSTNAME = 'SparkMonkey:Hostname'
INTENT_IP_ADDRESS = 'SparkMonkey:IPAddress'
INTENT_LATEST_SNIPS_VERSION = 'SparkMonkey:LatestSnipsVersion'
INTENT_LATEST_SNIPS_VERSION_RUNNING = 'SparkMonkey:LatestSnipsVersionRunning'
INTENT_SNIPS_VERSION = 'SparkMonkey:SnipsVersion'
INTENT_UPTIME = 'SparkMonkey:Uptime'
