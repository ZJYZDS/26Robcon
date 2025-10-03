#include <ros/ros.h>
#include <std_msgs/String.h>



int main(int argc, char* argv[])
{
    ros::init(argc,argv,"P_node");
    ros::NodeHandle n;
    ros::Publisher pub =n.advertise<std_msgs::String>("topic",10);
    ros::Rate rate(10);
    while(ros::ok())
    {
        std_msgs::String m;
        m.data="2023113135_张家源";
        pub.publish(m);
        rate.sleep();
    }
    return 0;
}
