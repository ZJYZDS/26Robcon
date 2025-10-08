import rospy
import rosbag
import open3d
import numpy as np
import sensor_msgs.point_cloud2  as pc2
import rosbags


class cropper:
    def __init__(self):
        pass

    def read_bag(self,bag_path,topic_name):
        bag = rosbag.Bag(bag_path,'r')# 以只读的mode open bag
        for topic , msg , _ in bag.read_messages(topics=[topic_name]):

            points = pc2.read_points_list(msg,field_names=['x','y','z'],skip_nans=True)
            # cloud = pcl.PointCloud().from_list(points)
            points_np = np.array(points,dtype=np.float64)

            cloud = open3d.geometry.PointCloud()
            cloud.points = open3d.utility.Vector3dVector(points_np)


            bag.close()

            return points , cloud

            


    def PointCloud_transformation(self,points):

#齐次变换矩阵判断（转换）
        if points.size[1] == 3:
            points_copy = np.hstack([points,np.ones(points.size[0],1,dtype=int)])
        else:
            points_copy = points
        

        transform_matrix=np.zeros(shape=(4,4),dtype=int)
        transform_matrix[0,0]=-1
        transform_matrix[1,1]=-1
        transform_matrix[2,2]=1
        transform_matrix[3,3]=1

        points_copy = np.dot(points_copy,transform_matrix)
        points = points_copy[:,:3]

        return points
    
#利用直通lubo
    def  passthrough_cloud(self,points):
        
        mask_x= (points[:,0] >= 0)&(points[:,0]<=5)
        mask_y= (points[:,1] >= 5)&(points[:,1]<=7)
        mask_z= (points[:2] >= 0.3)&(points[:,2]<=2)


        aim_points = []
        aim_points[:,0] = points[mask_x]
        aim_points[:,1] = points[mask_y]
        aim_points[:,2] = points[mask_z]

        if len(aim_points) == 0:
            print("error x,y,z")


        aim_cloud = open3d.geometry.PointCloud()
        aim_cloud.points = open3d.utility.Vector3dVector(aim_points)
        output_pcd_path = ""
        open3d.io.write_point_cloud(output_pcd_path,aim_cloud)#pcd file


        

if  __name__ == "__main__":
    # print(open3d.__version__)
    bag_path = ""
    topic_name = ""
    (points , cloud) = cropper.read_bag(bag_path,topic_name)
    cropper.passthrough_cloud(points)

