"""
Cold Email Agent - Project Structure Scaffolding Script (Python)

Usage:
    Open the terminal in VS Code within the directory where you want to create the project, 
    and run this script:

        python create_project_structure.py

This script will automatically generate the entire backend + frontend folder structure 
(including empty files), exactly as specified in the project plan.
"""
import os

ROOT = "cold-email-agent"

STRUCTURE = [
    # ---------------- Root ----------------
    ("docker-compose.yml", True),
    ("README.md", True),

    # ---------------- Backend ----------------
    ("backend", False),
    ("backend/Dockerfile", True),
    ("backend/requirements.txt", True),
    ("backend/.env", True),

    # backend/app
    ("backend/app", False),
    ("backend/app/main.py", True),
    ("backend/app/config.py", True),
    ("backend/app/database.py", True),

    # backend/app/models
    ("backend/app/models", False),
    ("backend/app/models/lead.py", True),
    ("backend/app/models/email_log.py", True),
    ("backend/app/models/campaign.py", True),
    ("backend/app/models/unsubscribe.py", True),

    # backend/app/schemas
    ("backend/app/schemas", False),
    ("backend/app/schemas/lead_schema.py", True),
    ("backend/app/schemas/email_schema.py", True),
    ("backend/app/schemas/stats_schema.py", True),

    # backend/app/services
    ("backend/app/services", False),
    ("backend/app/services/apollo_service.py", True),
    ("backend/app/services/llm_service.py", True),
    ("backend/app/services/email_service.py", True),

    # backend/app/graph
    ("backend/app/graph", False),
    ("backend/app/graph/state.py", True),
    ("backend/app/graph/nodes.py", True),
    ("backend/app/graph/graph_builder.py", True),

    # backend/app/scheduler
    ("backend/app/scheduler", False),
    ("backend/app/scheduler/scheduler.py", True),

    # backend/app/api
    ("backend/app/api", False),
    ("backend/app/api/routes_leads.py", True),
    ("backend/app/api/routes_campaigns.py", True),
    ("backend/app/api/routes_logs.py", True),
    ("backend/app/api/routes_stats.py", True),
    ("backend/app/api/routes_unsubscribe.py", True),

    # backend/app/utils
    ("backend/app/utils", False),
    ("backend/app/utils/logger.py", True),
    ("backend/app/utils/retry.py", True),

    # backend/alembic
    ("backend/alembic", False),

    # backend/tests
    ("backend/tests", False),
    ("backend/tests/test_apollo_service.py", True),
    ("backend/tests/test_graph_nodes.py", True),
    ("backend/tests/test_email_service.py", True),

    # ---------------- Frontend ----------------
    ("frontend", False),
    ("frontend/Dockerfile", True),
    ("frontend/package.json", True),
    ("frontend/vite.config.js", True),
    ("frontend/tailwind.config.js", True),

    # frontend/src
    ("frontend/src", False),
    ("frontend/src/main.jsx", True),
    ("frontend/src/App.jsx", True),

    # frontend/src/pages
    ("frontend/src/pages", False),
    ("frontend/src/pages/Dashboard.jsx", True),
    ("frontend/src/pages/Leads.jsx", True),
    ("frontend/src/pages/Campaigns.jsx", True),
    ("frontend/src/pages/EmailLogs.jsx", True),
    ("frontend/src/pages/Settings.jsx", True),

    # frontend/src/components
    ("frontend/src/components", False),
    ("frontend/src/components/Navbar.jsx", True),
    ("frontend/src/components/Sidebar.jsx", True),
    ("frontend/src/components/StatsCard.jsx", True),
    ("frontend/src/components/LeadsTable.jsx", True),
    ("frontend/src/components/LogsTable.jsx", True),

    # frontend/src/services
    ("frontend/src/services", False),
    ("frontend/src/services/api.js", True),

    # frontend/src/styles
    ("frontend/src/styles", False),
    ("frontend/src/styles/index.css", True),
]


def create_structure():
    print(f"Creating project root: {ROOT}")
    os.makedirs(ROOT, exist_ok=True)

    for rel_path, is_file in STRUCTURE:
        full_path = os.path.join(ROOT, rel_path)

        if is_file:
            # Make sure parent directory exists first
            parent_dir = os.path.dirname(full_path)
            if parent_dir:
                os.makedirs(parent_dir, exist_ok=True)
            # Create empty file only if it doesn't already exist
            if not os.path.exists(full_path):
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write("")
            print(f"  [file]  {full_path}")
        else:
            os.makedirs(full_path, exist_ok=True)
            print(f"  [dir]   {full_path}")

    print(f"\nProject structure successfully created inside '{ROOT}'.")


if __name__ == "__main__":
    create_structure()