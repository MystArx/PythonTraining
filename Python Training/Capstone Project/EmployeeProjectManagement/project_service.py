# Project Service Operations

from database import projects
from models import Project
from exceptions import ProjectNotFoundException, InvalidAllocationException
from logger_config import logger

def add_project(project_id, project_name, client_name, technology, duration, status="Active"):
    pid = str(project_id).strip().upper()
    for p in projects:
        if p.project_id == pid:
            print("Error: Project ID already exists.")
            return None
    if duration <= 0:
        print("Error: Duration must be greater than zero.")
        return None
    if status not in ["Active", "Completed", "Hold"]:
        print("Error: Status must be Active, Completed, or Hold.")
        return None

    new_proj = Project(pid, project_name.strip(), client_name.strip(), technology.strip(), duration, status.strip())
    projects.append(new_proj)
    logger.info(f"Project '{pid}' Created: {project_name}")
    return new_proj

def get_all_projects():
    return projects

def get_project_by_id(project_id):
    pid = str(project_id).strip().upper()
    for p in projects:
        if p.project_id == pid:
            return p
    raise ProjectNotFoundException(f"Project '{project_id}' not found.")

def search_projects(query):
    q = str(query).lower().strip()
    return [p for p in projects if q in p.project_id.lower() or q in p.project_name.lower() or q in p.technology.lower()]

def update_project(project_id, name=None, client=None, tech=None, duration=None, status=None):
    p = get_project_by_id(project_id)
    if name: p.project_name = name
    if client: p.client_name = client
    if tech: p.technology = tech
    if duration and duration > 0: p.project_duration = int(duration)
    if status in ["Active", "Completed", "Hold"]: p.project_status = status
    logger.info(f"Project '{project_id}' Updated")
    return p

def delete_project(project_id, allocated_projects=[]):
    p = get_project_by_id(project_id)
    if p.project_id in allocated_projects:
        raise InvalidAllocationException(f"Cannot delete Project '{project_id}': has active allocations.")
    projects.remove(p)
    logger.info(f"Project '{project_id}' Deleted")
    return p

def get_active_projects():
    return list(filter(lambda p: p.project_status == "Active", projects))
