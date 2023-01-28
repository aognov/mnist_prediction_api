pipeline{
  agent any
    stages { 
      stage('Building') {
        steps {
            // Install dependencies
            sh 'pip3 install -r requirements.txt'
        }
      }
      stage('Testing') {
        steps {
            sh 'python3 -m unittest'
        }
      }
      stage('Deploying') {
        steps {
          sh 'docker build -t aognov/mnist_prediction_api:latest .'
          sh 'docker run -d -p 6003:5000 aognov/mnist_prediction_api:latest'
        }
      }
    }
}
