from functools import total_ordering

@total_ordering
class Version():
    def __init__(self, string_version: str):
        self.major, self.minor, self.patch = Version.parse(string_version)

    @staticmethod
    def parse(str_version: str):
        vers = str_version.split('.')
        if len(vers) < 1 or len(vers) > 3:
            raise Exception('Wrong format')
        for ind, ver in enumerate(vers):
            try:
                vers[ind] = int(ver)
            except Exception as err:
                err_str = [
                    "Valid format is: major.minor.patch",
                    "Where major, minor and patch are integer more or equals 0",
                    err,
                ]
                raise Exception('\n'.join(err_str))
        while len(vers) < 3:
            vers.append(None)

        return vers[0], vers[1], vers[2]


    def __eq__(self, other):
        return (self.major == other.major) and \
            (self.minor == other.minor) and \
            (self.patch == self.patch)

    def __lt__(self, other):
        if self.major < other.major:
            return True
        if self.minor and other.minor and self.minor < other.minor:
            return True
        if self.minor and other.minor is None:
            return True
        if self.patch and other.patch and self.patch < other.patch:
            return True
        if self.patch and other.patch is None:
            return True


def compare_versions(version, other_version):
    ver = Version(version)
    other_ver = Version(other_version)
    if ver == other_ver:
        return 0
    if ver > other_ver:
        return 1
    return -1

if __name__ == '__main__':
    compare_versions('1.10', '1.1')
    compare_versions('1.8', '1.11')
    compare_versions('1.1', '1.1')
