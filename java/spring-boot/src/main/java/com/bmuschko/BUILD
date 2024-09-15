java_binary(
    name = "spring-boot-hello-world",
    srcs = glob(["src/main/java/**/*.java"]),
    main_class = "com.bmuschko.Application",
    runtime_deps  = [
        "@maven//:org_springframework_boot_spring_boot",
        "@maven//:org_springframework_boot_spring_boot_starter_web",
        "@maven//:org_springframework_boot_spring_boot_autoconfigure",
        "@maven//:org_springframework_spring_web",
    ],
)

java_library(
    name = "sample_code_library",
    srcs = ["SampleCode.java"],  # Use the filename only
    visibility = ["//src/test/func:__pkg__"],  # Allow visibility to the test package
)

java_library(
    name = "sample_code_library2",
    srcs = ["SampleCode2.java"],  # Use the filename only
    visibility = ["//src/test/func:__pkg__"],  # Allow visibility to the test package
)

java_library(
    name = "sample_code_library3",
    srcs = ["SampleCode3.java"],  # Use the filename only
    visibility = ["//src/test/func:__pkg__"],  # Allow visibility to the test package
)

java_library(
    name = "sample_code_library4",
    srcs = ["SampleCode4.java"],  # Use the filename only
    visibility = ["//src/test/func:__pkg__"],  # Allow visibility to the test package
)

java_library(
    name = "sample_code_library5",
    srcs = ["SampleCode5.java"],  # Use the filename only
    visibility = ["//src/test/func:__pkg__"],  # Allow visibility to the test package
)
