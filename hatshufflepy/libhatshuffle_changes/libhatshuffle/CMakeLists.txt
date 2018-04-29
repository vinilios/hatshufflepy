set(HATSHUFFLE_EXTRASRCS)
set(HATSHUFFLE_EXTRALIBS)

add_library(
  hatshuffle
  STATIC

  mixnet.cpp
  utils.cpp

  ${HATSHUFFLE_EXTRASRCS}
)
target_link_libraries(
  hatshuffle

  ff
  #GMP::gmp
  ${PROCPS_LIBRARIES}
  ${HATSHUFFLE_EXTRALIBS}
)
target_include_directories(
  hatshuffle
  PUBLIC ..
)

install(
  DIRECTORY "" DESTINATION "include/libhatshuffle"
  FILES_MATCHING
  PATTERN "*.hpp"
  PATTERN "*.tcc"
  PATTERN "tests" EXCLUDE
  PATTERN "examples" EXCLUDE
)

install(
  TARGETS hatshuffle DESTINATION lib
)

# add_executable(
  # multiexp_profile
  # EXCLUDE_FROM_ALL

  # algebra/scalar_multiplication/multiexp_profile.cpp
# )
# target_link_libraries(
  # multiexp_profile

  # ff
# )

# Tests
# if ("${IS_LIBFF_PARENT}")
  # add_executable(
    # algebra_bilinearity_test
    # EXCLUDE_FROM_ALL

    # algebra/curves/tests/test_bilinearity.cpp
  # )
  # target_link_libraries(
    # algebra_bilinearity_test

    # ff
  # )

  # add_executable(
    # algebra_groups_test
    # EXCLUDE_FROM_ALL

    # algebra/curves/tests/test_groups.cpp
  # )
  # target_link_libraries(
    # algebra_groups_test

    # ff
  # )

  # add_executable(
    # algebra_fields_test
    # EXCLUDE_FROM_ALL

    # algebra/fields/tests/test_fields.cpp
  # )
  # target_link_libraries(
    # algebra_fields_test

    # ff
  # )

  # include(CTest)
  # add_test(
    # NAME algebra_bilinearity_test
    # COMMAND algebra_bilinearity_test
  # )
  # add_test(
    # NAME algebra_groups_test
    # COMMAND algebra_groups_test
  # )
  # add_test(
    # NAME algebra_fields_test
    # COMMAND algebra_fields_test
  # )

  # add_dependencies(check algebra_bilinearity_test)
  # add_dependencies(check algebra_groups_test)
  # add_dependencies(check algebra_fields_test)
# endif()
