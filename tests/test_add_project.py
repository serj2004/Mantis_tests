

def test_add_project(app):
    app.session.login("administrator", "root")
    project_name = app.project.name_generator()
    old_project_list = app.project.get_project_list()
    app.project.add_new_project(project_name)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)


def test_delete_project(app):
    app.session.login("administrator", "root")
    old_project_list = app.project.get_project_list()
    if len(old_project_list) == 0:
        app.project.add_new_project('new')
    project_to_delete = old_project_list[0].name
    app.project.delete_project_by_name(project_to_delete)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)



