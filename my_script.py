import os
import sys

def check_onboarding_env():
    # 1. Check for a required environment variable (e.g., CLOUDBEES_API_KEY)
    api_key = os.getenv("CLOUDBEES_API_KEY")
    
    if not api_key:
        print("❌ Error: CLOUDBEES_API_KEY not found in environment.")
        sys.exit(1)
    
    print(f"✅ Environment Check: API Key is set (Length: {len(api_key)})")

    # 2. Check if the configuration file exists in the workspace
    config_file = "cloudbees-config.yaml"
    if os.path.exists(config_file):
        print(f"✅ Config Check: Found {config_file}")
    else:
        print(f"⚠️  Warning: {config_file} missing. Using default settings.")

if __name__ == "__main__":
    print("--- Starting Customer Environment Validation ---")
    check_onboarding_env()
    print("--- Validation Complete ---")