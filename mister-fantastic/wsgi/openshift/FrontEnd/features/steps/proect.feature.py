from behave import given, then, when
# project
@given(u'I am a visitor')
def i_am_a_visitor(context):
    pass

@when(u'I visit url "{url}"')
def impl(context, url):
    br = context.browser
    br.visit(url)

@when(u'fill in fields')
def impl(context):
    br = context.browser
    br.find_by_id('git').fill('https://NikitaTihonov@bitbucket.org/thegoodguysteam/mister-fantastic.git')
    br.find_by_id('username').fill('NikitaTihonov')
    br.find_by_id('password').fill('nikitatihonov')
    br.find_by_id("button").click()

@then(u'page url "{url}"')
def impl(context, url):
    br = context.browser
    u = br.url
    if u != url:
        assert False

@then(u'page have "Information about project"')
def impl(context):
    br = context.browser
    if not br.is_text_present('Information about project'):
        assert False



#project_team
@given(u'I visit url "{url}"')
def impl(context, url):
    br = context.browser
    br.visit(url)

@given(u'fill in fields')
def impl(context):
    br = context.browser
    br.find_by_id('git').fill('https://NikitaTihonov@bitbucket.org/thegoodguysteam/mister-fantastic.git')
    br.find_by_id('username').fill('NikitaTihonov')
    br.find_by_id('password').fill('nikitatihonov')
    br.find_by_id("button").click()

@when(u'click on "{click}"')
def impl(context, click):
    br = context.browser
    br.find_link_by_href(click).click()

@then(u'there id team')
def impl(context):
    br = context.browser
    team = br.find_by_id('team')
    if not team:
        assert False


# project_programmer
@then(u'there id programmer')
def impl(context):
    br = context.browser
    team = br.find_by_id('programmer')
    if not team:
        assert False


# language
@when(u'click on language')
def impl(context):
    br = context.browser
    br.find_by_id('language').click()
    
@then(u'there is a text "Statistics..."')
def impl(context):
    br = context.browser
    if not br.is_text_present('Statistics of your Git repositories'):
        assert False


#  Gppd Guys
@then(u'there is a href Good Guys')
def impl(context):
    br = context.browser
    assert br.find_link_by_href('//bitbucket.org/thegoodguysteam')


# team_project
@given(u'click on "{click}"')
def impl(context, click):
    br = context.browser
    br.find_link_by_href(click).click()

# team_programmer
# programmer_project
# programmer_team