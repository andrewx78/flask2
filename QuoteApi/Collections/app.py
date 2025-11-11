{
  "meta": {
    "format": "httpie",
    "version": "1.0.0",
    "contentType": "collection",
    "schema": "https://schema.httpie.io/1.0.0.json",
    "docs": "https://httpie.io/r/help/export-from-httpie",
    "source": "HTTPie Desktop 2025.2.0"
  },
  "entry": {
    "name": "QuotesAPI(Flask2)",
    "icon": {
      "name": "default",
      "color": "gray"
    },
    "auth": {
      "type": "none"
    },
    "requests": [
      {
        "name": "Lesson01 / Get a list of quotes",
        "url": "{{HOST}}{{PORT}}/quotes",
        "method": "GET",
        "headers": [],
        "queryParams": [],
        "pathParams": [],
        "auth": {
          "type": "inherited"
        },
        "body": {
          "type": "none",
          "file": {
            "name": ""
          },
          "text": {
            "value": "",
            "format": "application/json"
          },
          "form": {
            "isMultipart": false,
            "fields": []
          },
          "graphql": {
            "query": "",
            "variables": ""
          }
        }
      },
      {
        "name": "Lesson03 / Create new Author",
        "url": "{{HOST}}{{PORT}}/authors",
        "method": "POST",
        "headers": [],
        "queryParams": [],
        "pathParams": [],
        "auth": {
          "type": "inherited"
        },
        "body": {
          "type": "text",
          "file": {
            "name": ""
          },
          "text": {
            "value": "{\n  \"name\": \"Mark Twen\"\n}",
            "format": "application/json"
          },
          "form": {
            "isMultipart": false,
            "fields": []
          },
          "graphql": {
            "query": "",
            "variables": ""
          }
        }
      },
      {
        "name": "Lesson01 / Create new quote for Author",
        "url": "{{HOST}}{{PORT}}/authors/1/quotes",
        "method": "POST",
        "headers": [],
        "queryParams": [],
        "pathParams": [],
        "auth": {
          "type": "inherited"
        },
        "body": {
          "type": "text",
          "file": {
            "name": ""
          },
          "text": {
            "value": "{\n  \"text\": \"Mark's 2-nd quote\"\n}",
            "format": "application/json"
          },
          "form": {
            "isMultipart": false,
            "fields": []
          },
          "graphql": {
            "query": "",
            "variables": ""
          }
        }
      },
      {
        "name": "Lesson01 / Get all quotes of Author",
        "url": "{{HOST}}{{PORT}}/authors/1/quotes",
        "method": "GET",
        "headers": [],
        "queryParams": [],
        "pathParams": [],
        "auth": {
          "type": "inherited"
        },
        "body": {
          "type": "none",
          "file": {
            "name": ""
          },
          "text": {
            "value": "",
            "format": "application/json"
          },
          "form": {
            "isMultipart": false,
            "fields": []
          },
          "graphql": {
            "query": "",
            "variables": ""
          }
        }
      },
      {
        "name": "Lesson01 / Get quote by id",
        "url": "{{HOST}}{{PORT}}/quotes/2",
        "method": "GET",
        "headers": [],
        "queryParams": [],
        "pathParams": [],
        "auth": {
          "type": "inherited"
        },
        "body": {
          "type": "none",
          "file": {
            "name": ""
          },
          "text": {
            "value": "",
            "format": "application/json"
          },
          "form": {
            "isMultipart": false,
            "fields": []
          },
          "graphql": {
            "query": "",
            "variables": ""
          }
        }
      }
    ]
  }
}