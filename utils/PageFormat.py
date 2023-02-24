class toJson():
    @classmethod
    def page_format(self, data, pagequery):
        next=None
        prev=None
        page=pagequery.page
        per_page=pagequery.per_page
        pages = pagequery.pages
        count = pagequery.total
        if pagequery.has_next:
            next=pagequery.next_num
        if pagequery.has_prev:
            prev=pagequery.prev_num
        return {
            "data": data,
            "pagination": {
                "count": count,
                "page": page,
                "per_page": per_page,
                "pages": pages,
                "next":next,
                "prev":prev
            }
        }
