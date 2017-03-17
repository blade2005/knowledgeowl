"""KnowledgeOwl"""
from __future__ import print_function
import hammock

class MissingRequiredArg(Exception):
    def __init__(self, message):
        super(MissingRequiredArg, self).__init__(message)
        self.message = message
    def __repr__(self):
        print('Missing required argument: {0}'.format(self.message))


class KnowledgeOwl(object):
    def __init__(self, api_key, project_id):
        self.knowledgeowl = hammock.Hammock('https://app.knowledgeowl.com/api/head',
                                            auth=(api_key, 'X'))
        self.project_id = project_id

    def create_article(self, **kwargs):
        """Create KnowledgeOwl Article.

        Required: name, visibility, status, url_hash
        Optional: toc_title, category, application_screens, index,
                  category_view, prevent_searching, hide_from_toc, remove_pdf,
                  callout, callout_expire, callout_video, reader_roles,
                  current_version

        Notes: current_version should be an array ['en': {'text': '',
                                                          'title': ''}]
        """
        for key in ['name', 'visibility', 'status', 'url_hash']:
            if key not in kwargs.keys():
                raise MissingRequiredArg(key)
        kwargs['project_id'] = self.project_id
        return self.knowledgeowl('article.json').POST(data=kwargs).json()

    def list_articles(self):
        return self.knowledgeowl.article.GET().json()

    def get_article(self, article_id, replacesnippets=None, _fields=None):
        params = {}
        if replacesnippets:
            params['replaceSnippets'] = replacesnippets
        if _fields:
            params['_fields'] = _fields
        return self.knowledgeowl.article(article_id).GET(data={'_fields': 'current_version'},
                                                         params=params).json()

    def update_article(self, article_id, locale, html, title=None):
        """"""
        params = {'current_version': {locale: {'text': html}}}
        if title:
            params['current_version'][locale]['title'] = title
        return self.knowledgeowl.article('{0}.json'.format(article_id)).POST(data=params).json()

    def search_articles(self, phrase, status=None, _fields=None, limit=None):
        params = {}
        if status:
            params['status'] = status
        if _fields:
            params['_fields'] = _fields
        if limit:
            params['limit'] = limit
        return self.knowledgeowl.suggest.GET().json(data={'phrase': phrase},
                                                    params=params).json()

    def list_categories(self):
        return self.knowledgeowl.category.GET().json()

    def create_category(self, **kwargs):
        """Create KnowledgeOwl Article.

        Required: name, visibility, status, url_hash, type
        Optional: parent_id, toc_title, faq_display, toc_hide_children,
                  description, index, cat_toggle_override, reader_roles,
                  hide_from_toc

        """
        for key in ['name', 'visibility', 'status', 'url_hash', 'type']:
            if key not in kwargs.keys():
                raise MissingRequiredArg(key)
        kwargs['project_id'] = self.project_id
        return self.knowledgeowl('category.json').POST(data=kwargs).json()
