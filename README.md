# Formant ONVIF adapter
This adapter will allow for a robot to speak the text sent to it via Formant.

[Formant](https://formant.io) is a robot data and operations platform that allows companies to remotely manage all aspects of deployed systems, teleoperate them, and collect and analyze the sensor and telemetry data.

## Hardware
You'll need some speakers connected to your robot.

## Setup
### Install the Formant Agent
The agent should be installed before the adapter setup script is run.

SSH in to a the robot to run the installation script.

Follow the provided instructions to walk through the installation and provisioning process, skipping any references to ROS or Catkin as they are not used for this adapter.

### Command

The command filter is set to "speak_robot", so setup a command in your Formant front-end with that as the command. Enable parameters and use the parameter field to enter the text you want to speak.

### Details

Enter information on setup with pacmd and whatnot