from sanic import Sanic
from sanic import response


def main():
    app = Sanic('TestSanicApplication')

    app.run(host='localhost', port=8000, debug=True)


if __name__ == '__main__':
    main()
