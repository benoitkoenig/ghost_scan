tensorflowjs_converter --input_format keras scan/models/h5/remove_background.h5 scan/models/json/remove_background/ --weight_shard_size_bytes 419430400
tensorflowjs_converter --input_format keras scan/models/h5/detect_pose.h5 scan/models/json/detect_pose/ --weight_shard_size_bytes 419430400
tensorflowjs_converter --input_format keras scan/models/h5/finetune_positions.h5 scan/models/json/finetune_positions/ --weight_shard_size_bytes 419430400
