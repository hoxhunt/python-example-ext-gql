import requests


class HoxhuntApi:
    def __init__(self, auth_token, api_url):
        if auth_token == "" or api_url == "":
            raise Exception("Please provide auth_token & api_url")
        self.api_url = api_url
        self.headers = {"Authorization":
                        "Authtoken {}".format(auth_token)}

    def do_query(self, query, variables={}):
        request = requests.post(
            self.api_url,
            json={'query': query, 'variables': variables},
            headers=self.headers
        )
        if request.status_code == 200:
            return request.json()
        else:
            print(request.reason)
            raise Exception(
                "Query failed to run by returning code of {}. {}"
                .format(request.status_code, query))


class IncidentsIter:
    skip = 0
    first = 10

    def __init__(self, api_instance):
        self.api = api_instance

    def __next__(self):
        incidents = self.run_incidents_query()
        self.skip += 10
        self.first += 10
        return incidents

    def run_incidents_query(self):
        query = """query queryIncidentsWithIndicators($skip: Int, $first: Int) {
            incidents(first: $first, skip: $skip, sort: createdAt_DESC) {
                    createdAt
                    updatedAt
                    severity
                    policyName
                    lastReportedAt
                    firstReportedAt
                    threatCount
                    threats {
                        email {
                            from {
                                address
                            }
                            attachments {
                                hash
                            }
                            
                        }
                    enrichments {
                        hops {
                            from
                            by
                        }
                        links {
                            href
                            label
                        }
                    }
                    userModifiers {
                        userActedOnThreat
                        repliedToEmail
                        downloadedFile
                        openedAttachment
                        visitedLink
                        enteredCredentials
                        userMarkedAsSpam
                    }
                }
            }
        }"""
        variables = {'skip': self.skip, 'first': self.first}
        return self.api.do_query(query, variables)
