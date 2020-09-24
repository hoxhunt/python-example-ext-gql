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
            raise Exception(
                "Query failed to run by returning code of {}. {}"
                .format(request.status_code, query))

    def run_incidents_query(self):
        query = """ 
        query queryIncidentsWithIndicators {
            incidents(first: 10, skip: 0, sort: createdAt_DESC) {
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
        }
        """
        return self.do_query(query)
