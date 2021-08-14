from model.project import Project


def test_delete_project(app, config):
    app.session.login(config["webadmin"]["username"], config["webadmin"]["password"])
    old_project_list = app.project.get_project_list()
    if len(old_project_list) == 0:
        app.project.add_new_project('new')
    project_to_delete = old_project_list[0]
    app.project.delete_project_by_name(project_to_delete.name)
    old_project_list.remove(project_to_delete)
    new_project_list = app.project.get_project_list()
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
    app.session.logout()