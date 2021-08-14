from model.project import Project


def test_add_project(app):
    project_name = app.project.name_generator()
    old_project_list = app.project.get_project_list()
    app.project.add_new_project(project_name)
    new_project_list = app.project.get_project_list()
    added_project = sorted(new_project_list, key=Project.id_or_max)[-1]
    old_project_list.append(added_project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)





