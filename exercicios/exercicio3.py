from abc import ABC, abstractmethod


class SystemAccess(ABC):
    @abstractmethod
    def __init__(self):
        pass


class SupportSystemAccess(SystemAccess):
    def __init__(self):
        self.name = "Support"


class FinanceSystemAccess(SystemAccess):
    def __init__(self):
        self.name = "Finance"


class SalesSystemAccess(SystemAccess):
    def __init__(self):
        self.name = "Sales"


class Account(ABC):
    def __init__(self, username):
        self.username = username
        self.permissions = []
        self.create_account()

    @abstractmethod
    def create_account():
        pass

    def show_permissions(self):
        return [permission.name for permission in self.permissions]

    def add_permission(self, permission):
        self.permissions.append(permission)


class SupportAccount(Account):
    def create_account(self):
        self.add_permission(SupportSystemAccess())


class SupportAndSalesAccount(Account):
    def create_account(self):
        self.add_permission(SupportSystemAccess())
        self.add_permission(SalesSystemAccess())


class ManagerAccount(Account):
    def create_account(self):
        self.add_permission(SupportSystemAccess())
        self.add_permission(FinanceSystemAccess())
        self.add_permission(SalesSystemAccess())


if __name__ == "__main__":
    accounts = [
        SupportAccount("Beatriz"),
        SupportAndSalesAccount("Ana"),
        ManagerAccount("Carol"),
    ]

    for account in accounts:
        print(
            f"{account.username} tem acesso aos sistemas de: "
            f"{account.show_permissions()}"
        )
