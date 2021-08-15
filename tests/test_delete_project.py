from model.project import Project


def test_delete_project(app, config):
    old_project_list = app.soap.get_projects_list(config["webadmin"]["username"], config["webadmin"]["password"])
    if len(old_project_list) == 0:
        app.project.add_new_project('new')
    project_to_delete = old_project_list[0]
    app.project.delete_project_by_name(project_to_delete.name)
    old_project_list.remove(project_to_delete)
    new_project_list = app.soap.get_projects_list(config["webadmin"]["username"], config["webadmin"]["password"])
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)