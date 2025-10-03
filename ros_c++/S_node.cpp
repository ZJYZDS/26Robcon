#include<ros/ros.h>
#include<std_msgs/String.h>


void callback(std_msgs::String m)
{
    printf( m.data.c_str() );
    printf("\n");


}
int main(int argc, char* argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"S_node");
    ros::NodeHandle n;
    ros::Subscriber sub =n.subscribe("topic",10,callback);
    while(ros::ok())
    {
        ros::spin();
    }
    return 0;
}
