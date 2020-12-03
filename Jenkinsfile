///////////////////////////////////////////////////////////
// Call trans opt: received. 2-19-98 13:24:18 REC:Loc    //
//                                                       //
//      Trace program: running                           //
//                                                       //
//            wake up, Neo...                            //
//         the matrix has you                            //
//       follow the white rabbit.                        //
//                                                       //
//           knock, knock, Neo.                          //
//                                                       //
//                         (`.         ,-,               //
//                         ` `.    ,;' /                 //
//                          `.  ,'/ .'                   //
//                           `. X /.'                    //
//                 .-;--''--.._` ` (                     //
//               .'            /   `                     //
//              ,           ` '   Q '                    //
//              ,         ,   `._    \                   //
//           ,.|         '     `-.;_'                    //
//           :  . `  ;    `  ` --,.._;                   //
//            ' `    ,   )   .'                          //
//               `._ ,  '   /_                           //
//                  ; ,''-,;' ``-                        //
//                   ``-..__``--`                        //
///////////////////////////////////////////////////////////

GIT_CREDENTIAL = "tt-github-credential"
GIT_URL        = "https://github.com/kevout97/tt-2021-crud.git"
GIT_BRANCH     = "main"
GIT_PROYECT    = "tt-2021-crud"

AGENT_LABEL    = "jenkins-ckdply01-1"


pipeline{
    agent{
        label "${AGENT_LABEL}"
    }
    stages{
        stage("Clonning Source Code"){
            steps{
                sh"""
                    rm -rf *
                """
                git credentialsId: "${GIT_CREDENTIAL}" , url: "${GIT_URL}", branch: "${GIT_BRANCH}"
            }
        }

        stage("Build and push image"){
            steps{
                sh"""
                    ls -lha
                """
                script {
                    def customImage = docker.build("${JOB_NAME}:v${env.BUILD_ID}")
                    // customImage.push()
                }
            }
        }

        stage("Scanning"){
            parallel{
                stage("Scanning image"){
                    steps{
                        echo "Scanning image"
                    }
                }

                stage("Scanning source code"){
                    steps{
                        echo "Scanning source code"
                    }
                }
            }
        }

        stage("Prepare new deploy"){
            steps{
                echo "Deploy"
            }
        }

        stage("Deploying new image "){
            steps{
                echo "Test"
            }
        }

        stage("Create Report"){
            steps{
                echo "Test"
            }
        }
    }
    post{
        success{
            echo "Send notification"
        }
        failure{
            echo "Send notification"
        }
    }
}