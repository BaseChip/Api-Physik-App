from flask import request, jsonify
from flask_restful import Resource
from plots.beugungsmuster_plot import BeugungsmusterPlot


class Beugungsmuster(Resource):
    def get(self):
        spaltanzahl = request.args.get("spaltanzahl", 2)
        spaltabstand = request.args.get("spaltabstand", 1.0)
        wellenlaenge = request.args.get("wellenlaenge", 2.0)
        amplitude = request.args.get("amplitude", 1.0)
        name = BeugungsmusterPlot.create_plot(BeugungsmusterPlot(), int(spaltanzahl), float(spaltabstand), float(wellenlaenge), float(amplitude))
        return jsonify(filename=name)