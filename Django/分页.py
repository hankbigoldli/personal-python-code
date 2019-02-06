#by:hankli
class PageInfo(object):
    def __init__(self, current_page, per_page_num, all_count, url, show_page=11):
        '''

        :param current_page: 当前页面位置
        :param per_page_num: 每页显示数据的行数
        :param all_count: 数据库总行数
        :param url: 要提交的位置
        :param show_page: 分页要显示多长
        :param half: 当前位置往前往后显示的个数
        :param begin: 分页显示的首位置
        :param end: 分页显示的结束位置
        '''
        self.url = url  # 数据提交的地址
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.all_page, self.a = divmod(all_count, per_page_num)
        if self.a:
            self.all_page += 1

        self.half = int((show_page - 1) / 2)  # 当前页前五  后五
        if self.current_page <= self.half:
            # 前11页
            self.begain = 1
            self.end = show_page
        elif self.current_page >= (self.all_page - self.half):
            # 后11页
            self.begain = self.all_page - show_page
            self.end = self.all_page
        else:
            self.begain = self.current_page - self.half  # 前五开头
            self.end = self.current_page + self.half  # 后五结尾
        self.per_page_num = per_page_num

    def start_data(self):
        return (self.current_page - 1) * self.per_page_num

    def end_data(self):
        return self.current_page * self.per_page_num

    def page(self):
        page_list = []
        # 显示所有页
        if self.current_page > 1:
            temp = "<a style='display:inline-block;padding:5px;margin:5px;' href='%s?page=%s'>上一页</a>" % (
            self.url, self.current_page - 1,)
        else:
            temp = "<a style='display:inline-block;padding:5px;margin:5px;' href='#'>上一页</a>"
        page_list.append(temp)
        for i in range(self.begain, self.end + 1):
            if i == self.current_page:
                temp = "<a style='display:inline-block;padding:5px;margin:5px;background-color:red;' href='%s?page=%s'>%s</a>" % (
                self.url, i, i,)
            else:
                # if self.current_page <= 5:

                temp = "<a style='display:inline-block;padding:5px;margin:5px;' href='%s?page=%s'>%s</a>" % (
                self.url, i, i,)
            page_list.append(temp)
        if self.current_page >= self.all_page:
            temp = "<a style='display:inline-block;padding:5px;margin:5px;' href='#'>下一页</a>"
        else:
            temp = "<a style='display:inline-block;padding:5px;margin:5px;' href='%s?page=%s'>下一页</a>" % (
            self.url, self.current_page + 1,)
        page_list.append(temp)

        return "".join(page_list)
