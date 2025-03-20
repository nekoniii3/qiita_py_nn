class QiitaArticle:

    def __init__(self, dict_data):

        self.body = dict_data["body"]
        self.coediting = dict_data["coediting"]
        self.comments_count = dict_data["comments_count"]
        self.created_at = dict_data["created_at"]
        self.group = dict_data["group"]
        self.id = dict_data["id"]
        self.likes_count = dict_data["likes_count"]
        self.organization_url_name = dict_data["organization_url_name"]
        self.page_views_count = dict_data["page_views_count"]
        self.private = dict_data["private"]
        self.reactions_count = dict_data["reactions_count"]
        self.rendered_body = dict_data["rendered_body"]
        self.slide = dict_data["slide"]
        self.stocks_count = dict_data["stocks_count"]
        self.tags = dict_data["tags"]
        self.team_membership = dict_data["team_membership"]
        self.title = dict_data["title"]
        self.updated_at = dict_data["updated_at"]
        self.url = dict_data["url"]
        self.user = dict_data["user"]

    def __repr__(self):
        return f"QiitaArticle({vars(self)})"

class QiitaUser:

    def __init__(self, dict_data):

        self.description = dict_data["description"]
        self.facebook_id = dict_data["facebook_id"]
        self.followees_count = dict_data["followees_count"]
        self.followers_count = dict_data["followers_count"]
        self.github_login_name = dict_data["github_login_name"]
        self.id = dict_data["id"]
        self.items_count = dict_data["items_count"]
        self.linkedin_id = dict_data["linkedin_id"]
        self.location = dict_data["location"]
        self.name = dict_data["name"]
        self.organization = dict_data["organization"]
        self.permanent_id = dict_data["permanent_id"]
        self.profile_image_url = dict_data["profile_image_url"]
        self.team_only = dict_data["team_only"]
        self.twitter_screen_name = dict_data["twitter_screen_name"]
        self.website_url = dict_data["website_url"]