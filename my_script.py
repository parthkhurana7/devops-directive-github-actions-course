import os

# Check if a specific command is available in the customer's terminal
command = "docker --version"
status = os.system(command)

if status == 0:
    print("✅ Success: Tool is installed and ready for onboarding.")
else:
    print("❌ Error: Tool not found. Please install it before we proceed.")