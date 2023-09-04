import NaVi_pb2_grpc
import NaVi_pb2 as Navi
import grpc
import concurrent.futures as futures
import logging

# NaviServicer provides an implementation of the methods of the Navi service.
class NaviMockServer(NaVi_pb2_grpc.NaViServiceServicer):
    
    def __init__(self) -> None:
        self.__roverposition = Navi.Position3d(xMeter=0.0,yMeter=0.0,zMeter=0.0)
        self.__roverorientation = Navi.Quaternion(x=0.0,y=0.0,z=0.0,w=0.0)
        self.roverpose = Navi.Pose(position=self.__roverposition, orientation=self.__roverorientation)

    def __update_pose(self):
        self.__roverposition.xMeter+=1
        self.roverpose.position.xMeter+=1

    def getCurrentPose(self, request, context):
        self.__update_pose()
        logging.info(f"current pose: {self.roverpose}")
        return self.roverpose

def serve():
    port="50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    NaVi_pb2_grpc.add_NaViServiceServicer_to_server(
            NaviMockServer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()