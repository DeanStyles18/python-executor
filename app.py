from flask import Flask, request, jsonify
import sys
import io

app = Flask(__name__)

# Route to execute Python code
@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.json.get('code', '')

      output = io.StringIO()
    sys.stdout = output
    sys.stderr = output

    try:
        
        exec(code)
    except Exception as e:
                output.write(f"Error: {str(e)}")

   
    result = output.getvalue()
    sys.stdout = sys.__stdout__  # Reset stdout to default
    sys.stderr = sys.__stderr__  # Reset stderr to default

 
    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
