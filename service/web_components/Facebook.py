from flask import Flask, request, jsonify

class FacebookBackEnd(Component):
    def __init__(self, env:Environment):
        super.__init__(env, 'api/v1/facebook', FacebookBackEnd, ['GET', 'POST'])
        self.env = env

    def