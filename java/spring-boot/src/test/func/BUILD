java_test(
    name = "sample_code_test",
    srcs = ["SampleCodeTest.java"],
    deps = [
        "//src/main/java/com/bmuschko:sample_code_library",  # Dependency on the library target
        "//src/main/java/com/bmuschko:sample_code_library2",
        "//src/main/java/com/bmuschko:sample_code_library3",  # Dependency on the library target
        "//src/main/java/com/bmuschko:sample_code_library4",
        "@maven//:junit_junit",
    ],
    test_class = "func.SampleCodeTest",
    javacopts = ["-g"],
)